import numpy as np


class Neuron:

    def __init__(self, value=0):
        self.value = value
        self.bounded = []
        self.reverse_bounded = []
        self.calculated__weight = 0
        self.error = 0

    def set__value(self, value):
        self.value = value

    def set__weight(self, neuron, weight):
        for bound in self.bounded:
            if id(bound['neuron']) == id(neuron):
                bound['weight'] = weight

    def bind(self, neuron, weight):
        self.bounded.append({'neuron': neuron, 'weight': weight, 'error': 0})

    def reverse__bind(self, neuron):
        self.reverse_bounded.append({'neuron': neuron, 'error': 0})

    def get_bounded(self):
        return self.bounded

    def get__reverse_bounded(self):
        return self.reverse_bounded

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def sigmoid_dx(self):
        return self.value * (1 - self.value)

    def is__first_layer(self):
        if len(self.reverse_bounded) == 0:
            return True
        else:
            return False

    def calculate__weight(self):
        calculated = 0
        for reverse_bound in self.reverse_bounded:
            for bound in reverse_bound['neuron'].get_bounded():
                if id(bound['neuron']) == id(self):
                    calculated += (reverse_bound['neuron'].value * bound['weight'])
        if not self.is__first_layer():
            self.value = self.sigmoid(calculated)
