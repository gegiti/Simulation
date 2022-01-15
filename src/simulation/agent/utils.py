import numpy as np


def relu(v):
    return np.maximum(0, v)


def normalize(v):
    return v / np.sum(v)
