import numpy as np

from simulation.configuration import score


class Sensors(object):
    def __init__(self, creature):
        self.creature = creature
        self.available_cell = creature.land.available_cell
        self.input_length = 2

    @property
    def pos(self):
        return self.creature.pos

    @property
    def score(self):
        return score(self.creature)

    def get_state(self):
        return np.asarray(self.pos)
