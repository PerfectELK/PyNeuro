
from vendor.network.Network import Network

layers = [
    {
        'amount_neurons': 3,
        'begin__values': [1, 1, 1],
    },
    {
        'amount_neurons': 2,
        'begin__values': [55, 66]
    },
    {
        'amount_neurons': 2,
        'begin__values': [77, 99]
    },
]

network = Network(layers=layers)

for layer in network.layers:

    print("Layer begin")
    for neuron in layer.neurons:
        print('heuron start')
        print("neurons bounded")
        print(neuron.bounded)
        print(neuron.value)
        print("neurons reverse_bounded")
        print(neuron.reverse_bounded)
        print('heuron end')
    print("Layer end")







