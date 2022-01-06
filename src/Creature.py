
class Creature(object):
    def __init__(self, neurons, learn_rate):
        self.brain = Brain(neurons)
        self.learn_rate = learn_rate

    @property
    def actions(self):
        pass


class Brain(object):
    def __init__(self, neurons):
        self.graph = self.create_graph(neurons)

    @staticmethod
    def create_graph(neurons):
        pass