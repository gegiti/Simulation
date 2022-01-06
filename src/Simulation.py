import numpy as np

from .Creature import Creature


class Land(object):
    
    def __init__(self, width, length, ttl):
        self.width = width
        self.length = length
        self.grid = np.ndarray((width, length), Creature)
        self.ttl = ttl
        self._time = 0

    def time_step(self):
        self._time += 1

    def run(self):
        while self._time < self.ttl:
            self.time_step()
