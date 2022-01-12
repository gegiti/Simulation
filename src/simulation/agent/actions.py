import logging
from enum import Enum, auto


class Actions(Enum):

    NOTHING = auto()

    # TODO: Change this to Action.Move.NORTH
    # (name == 'Move', vlaue == (-1, 0)) or (a is Action.NOTHING, a is Action.MOVE).
    MOVE_NORTH = (-1, 0)
    MOVE_NORTH_EAST = (-1, 1)
    MOVE_EAST = (0, 1)
    MOVE_SOUTH_EAST = (1, 1)
    MOVE_SOUTH = (1, 0)
    MOVE_SOUTH_WEST = (1, -1)
    MOVE_WEST = (0, -1)
    MOVE_NORTH_WEST = (-1, -1)


def move(creature, action):
    _move(creature, calculate_move_index(creature.pos, action))


def calculate_move_index(position, action):
    assert action.name.startswith("MOVE"), "This is not a MOVE action"
    return tuple(action.value[i] + position[i] for i in range(len(position)))


def _move(creature, to_index):
    assert creature.land.available_cell(to_index), "Tried to move to an unavailable cell!"
    logging.action(creature, "Moving from {} to {}".format(creature.pos, to_index))
    creature.land.grid[to_index].creature = creature
    creature.land.grid[creature.pos].creature = None
    creature.pos = to_index
