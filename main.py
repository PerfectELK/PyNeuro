
from vendor.base_networks.with_teacher_network import WithTeacherNetwork

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

teacher = [
    [[1, 0, 1], 1],
    [[1, 1, 1], 1],
    [[0, 0, 1], 1],
    [[1, 0, 0], 1],
    [[0, 1, 0], 1],
    [[0, 0, 0], 0],
    [[0, 0, 0], 0],
]

network = WithTeacherNetwork(config=layers, teacher=teacher)

l0 = network.get__layer(0)

l0.set__after_layer__weights()













