import numpy as np

from .Creature import Creature


class Land(object):
    
    def __init__(self, land_args, creature_args):
        self._time = 0

        self._width, self._length, self._ttl, creature_percent = land_args
        self.creature_args = creature_args        

        self.grid = np.full((self._width, self._length), Cell())
        self.creature_amount = int(self.grid.size * creature_percent)
        self.init_grid()

    def iterate_grid(self):
        indices = list(np.ndindex(self.grid.shape))
        np.random.shuffle(indices)
        for index in indices:
            yield index

    def generate_creature(self, index):
        cell = self.grid[index]
        cell.creature = Creature(self, index, *self.creature_args)

    def init_grid(self):
        created = 0
        for index in self.iterate_grid():
            if created >= self.creature_amount:
                break
            self.generate_creature(index)
            created += 1
  
    def occupied(self, index):
        return self.grid[index].creature

    def time_step(self):
        self._time += 1
        for index in self.iterate_grid():
            if not self.occupied(index):
                continue
            self.grid[index].creature.take_action()

    def run(self):
        while self._time < self._ttl:
            self.time_step()


class Cell(object):

    def __init__(self):
        self.creature = None
        self.smell = None
        self.blocked = False