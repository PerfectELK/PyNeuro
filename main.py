from vendor.base_networks.with_teacher_network import WithTeacherNetwork
import sys

layers = [
    {
        'amount_neurons': 3,
        'begin__values': [1, 1, 1],
    },
    {
        'amount_neurons': 3,
        'begin__values': [],
    },
    {
        'amount_neurons': 1,
        'begin__values': []
    },
]

teacher = [
    [[1, 1, 1], 1],
    [[0, 0, 0], 0],
    [[1, 0, 0], 1],
    [[0, 0, 0], 0],
    [[1, 1, 0], 1],
    [[1, 0, 1], 1],
    [[0, 0, 0], 0],
]

network = WithTeacherNetwork(config=layers, teacher=teacher)


print(sys.getsizeof(network))

network.training()













