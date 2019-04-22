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

    def get__neuron(self, index):
        return self.neurons[index]

    def set__layer_values(self, values):
        for index in range(0, len(self.neurons)):
            item = self.neurons[index]
            item.set__value(values[index])

    def set__after_layer__weights_mass(self, weights=[]):
        our_neuron_index = 0
        external_neuron_index = 0
        for neuron in self.neurons:
            bounded = neuron.get_bounded()
            for bound in bounded:
                if weights[our_neuron_index][external_neuron_index] is not None:
                    bound['weight'] = weights[our_neuron_index][external_neuron_index]
                    external_neuron_index += 1
            our_neuron_index += 1

    def get__after_neurons(self):
        neurons = []
        for n in self.neurons:
            bounded = n.get_bounded()
            for bounded_neuron in bounded:
                neurons.append(bounded_neuron)
        return neurons

    def set__after_layer__weights(self, neurons=[]):
        after__neurons = self.get__after_neurons()
        for neuron in neurons:
            for after__neuron in after__neurons:
                if id(neuron['neuron']) == id(after__neuron['neuron']):
                    after__neuron['weight'] = neuron['neuron']

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
                    neuron.bind(after_neuron, random.random())

    def bind_before_layer(self):
        if(self.before_layer != None):
            before_neurons = self.before_layer.get__neurons()
            for neuron in self.neurons:
                for before_neuron in before_neurons:
                    neuron.reverse__bind(before_neuron)



