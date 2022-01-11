from enum import Enum, auto


class Action(Enum):

    NOTHING = auto()

    # TODO: Change this to Action.Move.NORTH (name == 'Move', vlaue == (-1, 0)) or (a is Action.NOTHING, a is Action.MOVE).
    MOVE_NORTH = (-1, 0)
    MOVE_NORTH_EAST = (-1, 1)
    MOVE_EAST = (0, 1)
    MOVE_SOUTH_EAST = (1, 1)
    MOVE_SOUTH = (1, 0)
    MOVE_SOUTH_WEST = (1, -1)
    MOVE_WEST = (0, -1)
    MOVE_NORTH_WEST = (-1, -1)
