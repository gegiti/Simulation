import numpy as np

from simulation.agent.utils import normalize, relu


class Net(object):
    def __init__(self, inputs, layers, outputs):
        params = []
        layers.append(outputs)
        n = inputs
        for m in layers:
            W = 2 * (np.random.rand(m, n) - 0.5)
            b = np.random.rand(m)
            params.append((W, b, relu))
            n = m
        self.params = params

    def run_net(self, inputs):
        v = inputs
        for W, b, activation in self.params:
            v = np.dot(W, v) + b
            v = activation(v)
        return normalize(v)
