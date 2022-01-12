import numpy as np


class Land(object):
    class Cell(object):
        def __init__(self):
            self.creature = None
            self.smell = None
            self.blocked = False

        def __int__(self):
            if self.blocked:
                return 128
            if self.creature:
                return 255
            return 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.array([[Land.Cell() for _ in range(self.width)] for _ in range(self.height)])

    def iterate_grid(self):
        indices = list(np.ndindex(self.grid.shape))
        np.random.shuffle(indices)
        for index in indices:
            yield index

    def available_cell(self, index):
        if not ((0 <= index[0] < self.height) and (0 <= index[1] < self.width)):
            return False
        elif self.grid[index].blocked:
            return False
        elif self.grid[index].creature:
            return False
        return True
