from enum import Enum, auto


class Creature(object):

    class Brain(object):

        def __init__(self, creature, neurons):
            self._creature = creature
            self.graph = self.create_graph(neurons)

        
        # Initializeation:

        @staticmethod
        def create_graph(neurons):
            pass

        
        # Sensors:

        @property
        def pos(self):
            return self._creature.pos

        @property
        def available_cell(self):
            return self._creature.land.available_cell


        # The brains main method:

        @property
        def action(self):
            """Choose what action to execute and return it."""
            to_index = tuple(Creature.Action.MOVE_EAST.value[i] + self.pos[i] for i in range(len(self.pos)))
            if self.available_cell(to_index):
                return Creature.Action.MOVE_EAST
            return Creature.Action.NOTHING

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
        self.brain = Creature.Brain(self, neurons)
        self.learn_rate = learn_rate

    def take_action(self):
        action = self.brain.action
        if action.name.startswith("MOVE"):
            to_index = tuple(action.value[i] + self.pos[i] for i in range(len(self.pos)))
            self.move(to_index)

    def move(self, to_index):
        assert self.land.available_cell(to_index), "Tried to move to an unzvailable cell!"
        self.land.grid[to_index].creature = self
        self.land.grid[self.pos].creature = None
        self.pos = to_index
