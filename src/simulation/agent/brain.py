from simulation.agent.actions import Action


class Brain(object):

    def __init__(self, creature, sensors, neurons):
        self.creature = creature
        self.sensors = sensors
        self.graph = self.create_graph(neurons)

    # For later use:
    @staticmethod
    def create_graph(neurons):
        pass

    # The brains main method:
    @property
    def action(self):
        """Choose what action to execute and return it."""
        to_index = tuple(Action.MOVE_EAST.value[i] + self.sensors.pos[i] for i in range(len(self.sensors.pos)))
        if self.sensors.available_cell(to_index):
            return Action.MOVE_EAST
        return Action.NOTHING
