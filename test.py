import numpy as np


class learning_neuron(object):

    def __init__(self,true_results):

        self.true_results = true_results
        self.weight_0_to_1 = np.random.normal(0.0, 2**-.5, (2, 3))
        self.weight_1_to_2 = np.random.normal(0.0, 2**-.5, (1, 2))
        self.count_input_data = 3
        self.count_neuron_1_layer = 2
        self.count_neuron_2_layer = 1

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def sigmoid_dx(self, x):
        return x * (1 - x)

    def print_true_res(self):
        print(self.true_results)

    def print_weights_res(self):
        print("weights 1 layer: ", self.weight_0_to_1)
        print("weights 2 layer: ", self.weight_1_to_2)

    def addition_input_info(self, layer_neurons, layer_weight):
        info = 0
        i = 0
        while i < len(layer_weight):
            info += (layer_neurons[i] * layer_weight[i])
            i += 1
        s = self.sigmoid(info)
        return s




true_results = [
    ([1, 0, 1], 1),
    ([1, 1, 1], 1),
    ([0, 0, 0], 0),
    ([0, 0, 1], 1),
    ([1, 0, 0], 1),
    ([0, 0, 1], 1),
    ([0, 0, 0], 0),
    ([0, 0, 0], 0),
    ([0, 1, 0], 1),
]

learn = learning_neuron(true_results)


print(learn.addition_input_info(true_results[0][0], learn.weight_0_to_1[0]))

print(learn.sigmoid(learn.addition_input_info(true_results[0][0], learn.weight_0_to_1[0])))

