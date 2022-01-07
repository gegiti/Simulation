from enum import Enum, auto


class Creature(object):

    class Brain(object):

        def __init__(self, neurons):
            self.graph = self.create_graph(neurons)

        @staticmethod
        def create_graph(neurons):
            pass

    class Action(Enum):
        NOTHING = auto()
        MOVE_NORTH = (1, 0)
        MOVE_NORTH_EAST = (1, -1)
        MOVE_EAST = (0, -1)
        MOVE_SOUTH_EAST = (-1, -1)
        MOVE_SOUTH = (-1, 0)
        MOVE_SOUTH_WEST = (-1, 1)
        MOVE_WEST = (0, 1)
        MOVE_NORTH_WEST = (1, 1)

    def __init__(self, land, pos, neurons, learn_rate):
        self.land = land
        self.pos = pos
        self.brain = Creature.Brain(neurons)
        self.learn_rate = learn_rate

    @property
    def action(self):
        """Choose what action to do and return it."""
        to_index = tuple(Creature.Action.MOVE_EAST.value[i] + self.pos[i] for i in range(len(self.pos)))
        if not self.land.occupied(to_index) and ((0 <= to_index[0] < self.land._width) and (0 <= to_index[1] < self.land._height)):
            return Creature.Action.MOVE_EAST
        return Creature.Action.NOTHING

    def take_action(self):
        action = self.action
        if action.name.startswith("MOVE"):
            to_index = tuple(action.value[i] + self.pos[i] for i in range(len(self.pos)))
            self.move(to_index)

    def move(self, to_index):
        assert not self.land.occupied(to_index), "Tried to move to an occupied cell!"
        assert (0 <= to_index[0] < self.land._width) and (0 <= to_index[1] < self.land._height), "Tried to move out of the land!"
        self.land.grid[to_index].creature = self
        self.land.grid[self.pos].creature = None
        self.pos = to_index
