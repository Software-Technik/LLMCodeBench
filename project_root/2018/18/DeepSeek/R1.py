import numpy as np
from timeit import default_timer
import sys


class NoCycleFound(Exception):
    pass


class Lumberyard:
    def __init__(self, file_name: str, max_iter: int=10_000) -> None:
        if max_iter < 10:
            raise ValueError("The iteration limit needs to be at least 10")

        self.start_time = default_timer()

        self.max_iter: int = max_iter
        self.iterations_needed: int

        self.land: np.array = Lumberyard.file_to_array(file_name)
        self.neighbors: np.array = np.zeros(self.land.shape, dtype=int)

    @staticmethod
    def file_to_array(fn: str) -> np.array:
        m = {".": 1, "|": 10, "#": 100}

        with open(fn) as raw_data:
            data = [[m[c] for c in row.strip()] for row in raw_data]

        cols = len(data[0])
        rows = len(data)

        land = np.zeros((cols+2, rows+2), dtype=int)
        land[1:-1, 1:-1] = data
        return land

    def calculate_neighbors(self) -> None:
        box = np.cumsum(self.land, axis=1, dtype=int)
        box[:, 3:] = box[:, 3:] - box[:, :-3]
        box = np.cumsum(box, axis=0, dtype=int)
        box[3:, :] = box[3:, :] - box[:-3, :]
        self.neighbors[1:-1, 1:-1] = box[2:, 2:] - self.land[1:-1, 1:-1]

    def advance_minute(self) -> None:
        self.calculate_neighbors()

        neighbors_100 = self.neighbors % 100

        empty = self.land == 1
        trees = self.land == 10
        lumber = self.land == 100

        self.land[np.logical_and(empty, neighbors_100 >= 30)] = 10
        self.land[np.logical_and(trees, self.neighbors >= 300)] = 100

        lumber_friendly = np.logical_and(self.neighbors >= 100, neighbors_100 >= 10)
        self.land[np.logical_and(lumber, lumber_friendly)] = 100
        self.land[np.logical_and(lumber, np.logical_not(lumber_friendly))] = 1

    def run_until_cycle(self) -> None:
        self.land_values = []
        self.history = {}

        for minute in range(1, self.max_iter+1):
            self.advance_minute()
            value = (self.land == 10).sum() * (self.land == 100).sum()
            self.land_values.append(value)

            state_hash = hash(self.land.tobytes())
            if state_hash in self.history:
                prev_minute = self.history[state_hash]
                self.cycle_start = prev_minute
                self.cycle_length = minute - prev_minute
                self.iterations_needed = minute
                break
            else:
                self.history[state_hash] = minute
        else:
            raise NoCycleFound("No cycle found within the specified number of iterations")

        self.answer_one = self.land_values[9]

        if 1000000000 < self.cycle_start:
            self.answer_two = self.land_values[1000000000-1]
        else:
            offset = (1000000000 - self.cycle_start) % self.cycle_length
            index = self.cycle_start - 1 + offset
            self.answer_two = self.land_values[index]

        self.end_time = default_timer()
        self.duration = self.end_time - self.start_time


if __name__ == "__main__":
    input_f = sys.argv[1]
    collection_area = Lumberyard(input_f)
    collection_area.run_until_cycle()

    sys.stdout.write(f"{collection_area.answer_one} {collection_area.answer_two}")