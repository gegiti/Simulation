import numpy as np
import random

from simulation.agent.actions import Actions, calculate_move_index


class Brain(object):
    def __init__(self, creature, sensors, layers, learn_rate):
        self.creature = creature
        self.sensors = sensors
        self.net = self.create_net(sensors, layers, len(Actions))
        self.learn_rate = learn_rate

    # For later use:
    @staticmethod
    def create_net(inputs, layers, outputs):
        pass

    def is_action_possible(self, action):
        if action is Actions.NOTHING:
            return True
        if action.name.startswith("MOVE"):
            return self.sensors.available_cell(calculate_move_index(self.sensors.pos, action))

    # The brains main method:
    @property
    def action(self):
        """Choose what action to execute and return it."""
        # action = random.choice(list(Actions))
        action = Actions.MOVE_NORTH_EAST
        if self.is_action_possible(action):
            return action
        return Actions.NOTHING
