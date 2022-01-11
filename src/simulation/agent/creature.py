import logging

from simulation.agent.brain import Brain
from simulation.agent.sensors import Sensors


class Creature(object):

    def __init__(self, land, pos, neurons, learn_rate):
        self.land = land
        self.pos = pos
        self.brain = Brain(self, Sensors(self), neurons, learn_rate)

    def take_action(self):
        action = self.brain.action
        if action.name.startswith("MOVE"):
            to_index = tuple(action.value[i] + self.pos[i] for i in range(len(self.pos)))
            self.move(to_index)

    def move(self, to_index):
        assert self.land.available_cell(to_index), "Tried to move to an unavailable cell!"
        logging.debug("Moving from {} to {}".format(self.pos, to_index))
        self.land.grid[to_index].creature = self
        self.land.grid[self.pos].creature = None
        self.pos = to_index
