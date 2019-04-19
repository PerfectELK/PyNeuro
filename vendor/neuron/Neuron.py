import numpy as np


class Neuron:


    def __init__(self, value=0):
        self.value = value
        self.bounded = []
        self.reverse_bounded = []
        self.calculated__weight = 0
        self.bounded_weight_error = 0

    def bind(self, neuron, weight):
        self.reverse_bounded.append({'neuron': neuron, 'weight': weight})

    def reverse__bind(self, neuron):
        self.bounded.append({'neuron': neuron})

    def get_bounded(self):
        return self.bounded

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def sigmoid_dx(self):
        return self.calculated__weight * (1 - self.calculated__weight)

    def calculate__weight(self):
        calculated = 0
        for bound in self.bounded:
            calculated += bound.weight * bound.neuron.value
        self.calculated__weight = self.sigmoid(calculated)
        return self
