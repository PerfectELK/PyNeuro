import random
from vendor.neuron.Neuron import Neuron


class Layer:

    def __init__(self, amount_neurons, begin__values=[]):
        self.amount_neurons = amount_neurons
        self.before_layer = None
        self.after_layer = None
        self.neurons = []
        self.begin__values = begin__values

    def create_neighbours_layers(self, before_layer=None, after_layer=None):
        self.before_layer = before_layer
        self.after_layer = after_layer
        return self

    def get__neurons(self):
        return self.neurons

    def create_neurons(self):
        for num in range(0, self.amount_neurons):
            if(len(self.begin__values)):
                neuron = Neuron(value=self.begin__values[num])
            else:
                neuron = Neuron()
            self.neurons.append(neuron)
        return self

    def bind_after_layer(self):
        if(self.after_layer != None):
            after_neurons = self.after_layer.get__neurons()
            for neuron in self.neurons:
                for after_neuron in after_neurons:
                    neuron.bind(after_neuron,random.random())

    def bind_before_layer(self):
        if(self.before_layer != None):
            before_neurons = self.before_layer.get__neurons()
            for neuron in self.neurons:
                for before_neuron in before_neurons:
                    neuron.reverse__bind(before_neuron)



