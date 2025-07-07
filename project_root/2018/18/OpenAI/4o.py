import numpy as np
import sys


class NoCycleFound(Exception):
    pass


class Lumberyard:
    def __init__(self, file_name: str, max_iter: int = 10_000) -> None:
        if max_iter < 10:
            raise ValueError("The iteration limit needs to be at least 10")

        self.max_iter = max_iter
        self.land = self.file_to_array(file_name)
        self.neighbors = np.zeros(self.land.shape, dtype=int)
        self.land_hashes = {}
        self.land_values = []

    @staticmethod
    def file_to_array(fn: str) -> np.array:
        m = {".": 1, "|": 10, "#": 100}
        with open(fn) as raw_data:
            data = [[m[c] for c in row.strip()] for row in raw_data]
        cols = len(data[0])
        rows = len(data)
        land = np.zeros((cols + 2, rows + 2), dtype=int)
        land[1:-1, 1:-1] = data
        return land

    def calculate_neighbors(self) -> None:
        box = np.cumsum(self.land, axis=1, dtype=int)
        box[:, 3:] -= box[:, :-3]
        box = np.cumsum(box, axis=0, dtype=int)
        box[3:, :] -= box[:-3, :]
        self.neighbors[1:-1, 1:-1] = box[2:, 2:] - self.land[1:-1, 1:-1]

    def advance_minute(self) -> None:
        self.calculate_neighbors()

        neighbors_100 = self.neighbors % 100

        np.place(self.land, (self.land == 1) & (neighbors_100 >= 30), 10)
        np.place(
            self.land,
            (self.land == 10) & (self.neighbors >= 300),
            100,
        )

        lumber_friendly = (self.neighbors >= 100) & (neighbors_100 >= 10)
        np.place(self.land, (self.land == 100) & lumber_friendly, 100)
        np.place(self.land, (self.land == 100) & ~lumber_friendly, 1)

    def run_until_cycle(self) -> None:
        for current_iter in range(self.max_iter):
            self.advance_minute()
            value = (self.land == 10).sum() * (self.land == 100).sum()

            land_hash = hash(self.land.tobytes())
            if land_hash in self.land_hashes:
                self.cycle_start = self.land_hashes[land_hash]
                self.cycle_length = current_iter - self.cycle_start
                break

            self.land_values.append(value)
            self.land_hashes[land_hash] = current_iter
        else:
            raise NoCycleFound("No cycle found within the specified number of iterations")

        self.answer_one = self.land_values[9]

        self.location_in_cycle = (1_000_000_000 - self.cycle_start) % self.cycle_length
        answer_index = self.cycle_start + self.location_in_cycle - 1
        self.answer_two = self.land_values[answer_index]


if __name__ == "__main__":
    input_f = sys.argv[1]
    collection_area = Lumberyard(input_f)
    collection_area.run_until_cycle()

    sys.stdout.write(f"{collection_area.answer_one} {collection_area.answer_two}")