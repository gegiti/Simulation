from simulation.agent.actions import move
from simulation.agent.brain import Brain
from simulation.agent.sensors import Sensors


class Creature(object):
    def __init__(self, land, pos, layers, learn_rate):
        self.land = land
        self.pos = pos
        self.brain = Brain(self, Sensors(self), layers, learn_rate)

    def take_action(self):
        action = self.brain.action
        if action.name.startswith("MOVE"):
            move(self, action)
