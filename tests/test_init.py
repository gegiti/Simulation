
from src.Creature import Creature
from src.Simulation import Land


def test_land(fix):
    width = 100
    length = 100
    ttl = 100
    Land(width, length, ttl)


def test_creature(fix):
    neurons = 4
    learn_rate = 0.03
    Creature(neurons, learn_rate)
