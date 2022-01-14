import numpy as np

from simulation.agent.actions import Actions, calculate_move_index


class Brain(object):
    def __init__(self, creature, sensors, layers, learn_rate):
        self.creature = creature
        self.sensors = sensors
        self.net = self.create_net(sensors.input_length, layers, len(Actions))
        self.learn_rate = learn_rate

    @staticmethod
    def create_net(inputs, layers, outputs):
        net = []
        layers.append(outputs)
        n = inputs
        for m in layers:
            W = 2 * (np.random.rand(m, n) - 0.5)
            b = np.random.rand(m)
            net.append((W, b))
            n = m
        return net

    def run_net(self, inputs):
        v = inputs
        for W, b in self.net:
            v = np.dot(W, v) + b
            v = self.relu(v)
        action_index = np.random.choice(len(Actions), p=self.normalize(v))
        return list(Actions)[action_index]

    @staticmethod
    def relu(v):
        return np.maximum(0, v)

    @staticmethod
    def normalize(v):
        return v / sum(v)

    def is_action_possible(self, action):
        if action is Actions.NOTHING:
            return True
        if action.name.startswith("MOVE"):
            return self.sensors.available_cell(calculate_move_index(self.sensors.pos, action))

    # The brains main method:
    @property
    def action(self):
        """Choose what action to execute and return it."""
        inputs = self.sensors.get_state()
        action = self.run_net(inputs)
        # action = np.random.choice(Actions)
        # action = Actions.MOVE_NORTH_EAST
        if self.is_action_possible(action):
            return action
        return Actions.NOTHING
