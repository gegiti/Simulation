import numpy as np

from .Creature import Creature


class Land(object):
    
    def __init__(self, land_args, creature_args):
        self._time = 0

        self._width, self._length, self._ttl, creature_percent = land_args
        self.creature_args = creature_args        

        self.grid = np.ndarray((self._width, self._length), Creature)
        self.creature_amount = int(self.grid.size * creature_percent)
        self.init_grid(self.grid, self.creature_amount)

    def generate_creature(self):
        return Creature(*self.creature_args)

    def init_grid(self, grid, creature_amount):
        indices = list(np.ndindex(grid.shape))
        np.random.shuffle(indices)
        for index in indices[:creature_amount]:
            grid[index] = self.generate_creature()
    
    def time_step(self):
        self._time += 1

    def run(self):
        while self._time < self._ttl:
            self.time_step()
