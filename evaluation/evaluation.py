import pandas as pd
import plotly.express as px
from scipy.stats import wilcoxon
from tabulate import tabulate
import sqlite3

class Evaluation:
    def __init__(self, db_path):
        self.db_path = db_path
        self._load_data_from_sqlite()
        self._prepare_data()

    def _load_data_from_sqlite(self):
        conn = sqlite3.connect(self.db_path)
        self.df = pd.read_sql_query("SELECT * FROM results", conn)
        conn.close()

    def _prepare_data(self):
        df = self.df
        df.columns = df.columns.str.strip().str.lower()
        df = df[df['correct'].str.upper() == 'YES'].copy()

        df['runtime_ms'] = df['runtime_ms'].astype(float)
        df['memory_kb'] = df['peak_mem_kb'].astype(float).astype(int)
        df['runtime_x_mem'] = df['runtime_ms'] * df['memory_kb']

        def extract_parts(path):
            parts = path.split('/')
            if len(parts) == 4:
                year, exp, company, model = parts
            elif len(parts) == 3:
                year, exp, model = parts
                company = 'human'
            else:
                return pd.Series([None] * 4)
            return pd.Series([int(year), int(exp), company, model])

        df[['year', 'experiment', 'company', 'model']] = df['filename'].apply(extract_parts)
        df.dropna(subset=['year', 'experiment', 'company', 'model'], inplace=True)

        def sort_key(row):
            company_order = {"openai": 0, "deepseek": 1, "ollama": 2 ,"human": 3}
            model_type = 1 if "reasoning" in row["model"].lower() else 0
            return (company_order.get(row["company"].lower(), 99), model_type, row["model"])

        df = df.sort_values(by=["company", "model"], key=lambda col: df.apply(sort_key, axis=1))
        df['model'] = pd.Categorical(df['model'], categories=df['model'].unique(), ordered=True)
        df['task_id'] = df['year'].astype(str) + "_" + df['experiment'].astype(str) + "_" + df['expected_solution'].astype(str)


        self.df = df

    def plot_box(self, y_column, title, y_label):
        fig = px.box(
            self.df,
            x='model',
            y=y_column,
            log_y=True,
            title=title,
            points="all",
            labels={y_column: y_label, "model": "Modell"},
            hover_data=["company", "experiment"]
        )
        fig.update_layout(height=600)
        fig.show()

    def plot_all(self):
        self.plot_box("runtime_ms", "Laufzeitvergleich", "Runtime (ms)")
        self.plot_box("memory_kb", "Speicherverbrauch", "Memory (kB)")
        self.plot_box("runtime_x_mem", "Laufzeit × Speicher", "Runtime × Memory")

    def run_wilcoxon_tests(self, metric="runtime_x_mem"):
        vergleich = []
        df = self.df
        human = df[df['model'] == 'human.py']

        for modell_name in df['model'].unique():
            if modell_name == 'human.py':
                continue

            modell = df[df['model'] == modell_name]
            joined = pd.merge(modell, human, on="task_id", suffixes=('_modell', '_human'))

            if len(joined) < 3:
                continue

            try:
                stat, p = wilcoxon(
                    joined[f'{metric}_modell'],
                    joined[f'{metric}_human'],
                    alternative='less'
                )

                median_human = joined[f'{metric}_human'].median()
                median_modell = joined[f'{metric}_modell'].median()
                delta = median_human - median_modell
                rel_diff = delta / median_human

                n_besser = (joined[f'{metric}_modell'] < joined[f'{metric}_human']).sum()
                n_schlechter = len(joined) - n_besser

                vergleich.append({
                    "Modell": modell_name,
                    "Vergleichspaare": len(joined),
                    "T-Wert": stat,
                    "p-Wert": round(p, 6),
                    "Signifikant (p<0.001)": p < 0.001,
                    "Median_human": round(median_human, 2),
                    "Median_modell": round(median_modell, 2),
                    "Δ_abs": round(delta, 2),
                    "Verbesserung": round(rel_diff, 4),
                    "Anzahl_besser": n_besser,
                    "Anzahl_schlechter": n_schlechter
                })
            except Exception as e:
                print(f"Fehler bei Modell {modell_name}: {e}")

        vergleich.sort(key=lambda x: x['Verbesserung'], reverse=True)
        return vergleich


    def export_wilcoxon_results(self, metric="runtime_x_mem"):
        results = self.run_wilcoxon_tests(metric=metric)

        for v in results:
            v["% besser"] = round(v["Anzahl_besser"] / v["Vergleichspaare"] * 100, 1)
            v["% schlechter/gleich"] = round(v["Anzahl_schlechter"] / v["Vergleichspaare"] * 100, 1)

        df_results = pd.DataFrame(results)
        output_path = f"{metric}.csv"
        df_results.to_csv(output_path, index=False)

        print(f"Metrik: {metric}")

        headers = [
            "Modell", "n", "T-Wert", "p-Wert",
            "Med. Human", "Med. Modell", "Δ_abs", "Verbesserung",
            "besser", "% besser", "schlechter", "% schlechter/gleich"
        ]

        table = []
        for v in results:
            table.append([
                v["Modell"],
                v["Vergleichspaare"],
                f"{v['T-Wert']:.1f}",
                f"{v['p-Wert']:.6f}",
                f"{v['Median_human']:.2f}",
                f"{v['Median_modell']:.2f}",
                f"{v['Δ_abs']:.2f}",
                f"{v['Verbesserung']:.4%}",
                v["Anzahl_besser"],
                f"{v['% besser']}%",
                v["Anzahl_schlechter"],
                f"{v['% schlechter/gleich']}%"
            ])

        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    
    def _load_data_from_sqlite(self):
            conn = sqlite3.connect(self.db_path)
            self.df = pd.read_sql_query("SELECT * FROM results", conn)
            conn.close()
            print("Geladene Spalten:", self.df.columns.tolist())
if __name__ == "__main__":
    analyzer = Evaluation("results.db")
    analyzer.export_wilcoxon_results("runtime_ms")
    analyzer.export_wilcoxon_results("memory_kb")
    analyzer.export_wilcoxon_results("runtime_x_mem")
