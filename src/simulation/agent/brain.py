import numpy as np

from simulation.agent.actions import Actions, calculate_move_index
from simulation.agent.net import Net


class Brain(object):
    def __init__(self, creature, sensors, layers, learn_rate):
        self.creature = creature
        self.sensors = sensors
        self.net = Net(sensors.input_length, layers, len(Actions))
        self.learn_rate = learn_rate

    def is_action_possible(self, action):
        if action is Actions.NOTHING:
            return True
        if action.name.startswith("MOVE"):
            return self.sensors.available_cell(calculate_move_index(self.sensors.pos, action))

    @property
    def action(self):
        """Choose what action to execute and return it."""
        inputs = self.sensors.get_state()
        weights_vec = self.net.run_net(inputs)
        action = np.random.choice(Actions, p=weights_vec)
        # action = np.random.choice(Actions)
        # action = Actions.MOVE_NORTH_EAST
        if self.is_action_possible(action):
            return action
        return Actions.NOTHING
