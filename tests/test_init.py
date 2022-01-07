
from src.Creature import Creature
from src.Simulation import Land


def test_land(fix):
    width = 100
    length = 100
    ttl = 100
    creature_percentage = 0.2
    neurons = 4
    learn_rate = 0.03
    Land((width, length, ttl, creature_percentage), (neurons, learn_rate))


def test_creature(fix):
    neurons = 4
    learn_rate = 0.03
    Creature(neurons, learn_rate)
