from enum import Enum, auto


class Creature(object):
    def __init__(self, neurons, learn_rate):
        self.brain = Brain(neurons)
        self.learn_rate = learn_rate

    @property
    def action(self):
        return Action.NOTHING


class Brain(object):
    def __init__(self, neurons):
        self.graph = self.create_graph(neurons)

    @staticmethod
    def create_graph(neurons):
        pass

class Action(Enum):
    NOTHING = auto()
    MOVE_NORTH = auto()
    MOVE_NORTH_EAST = auto()
    MOVE_EAST = auto()
    MOVE_SOUTH_EAST = auto()
    MOVE_SOUTH = auto()
    MOVE_SOUTH_WEST = auto()
    MOVE_WEST = auto()
    MOVE_NORTH_WEST = auto()