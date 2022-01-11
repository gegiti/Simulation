from simulation.configuration import score


class Sensors(object):

    def __init__(self, creature):
        self.creature = creature
        self.available_cell = creature.land.available_cell

    @property
    def pos(self):
        return self.creature.pos

    @property
    def score(self):
        return score(self.creature)
