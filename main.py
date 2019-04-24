from vendor.base_networks.with_teacher_network import WithTeacherNetwork
import sys

layers = [
    {
        'amount_neurons': 6,
        'begin__values': [1, 1, 1, 1, 1, 1],
    },
    {
        'amount_neurons': 8,
        'begin__values': [1, 1, 1, 1, 1, 1, 1, 1],
    },
    {
        'amount_neurons': 4,
        'begin__values': [1, 1, 1, 1],
    },
    {
        'amount_neurons': 2,
        'begin__values': []
    },
]

teacher = [
    [[1, 1, 1, 0, 0, 0], [1, 0]],
    [[0, 0, 0, 1, 1, 1], [0, 1]],
    [[0, 0, 0, 1, 0, 1], [0, 1]],
    [[1, 1, 1, 1, 0, 1], [1, 1]],
    [[1, 0, 1, 1, 0, 1], [1, 1]],
    [[0, 1, 1, 0, 1, 1], [1, 1]],
    [[1, 1, 0, 1, 1, 0], [1, 1]],
]
# teacher = [
#     [[1, 1, 1], [1]],
#     [[0, 0, 0], [0]],
#     [[1, 0, 0], [1]],
#     [[0, 0, 0], [0]],
#     [[1, 1, 0], [1]],
#     [[1, 0, 1], [1]],
#     [[0, 1, 1], [0]],
#     [[0, 0, 1], [1]],
# ]

network = WithTeacherNetwork(config=layers, teacher=teacher)

network.training()

values = [
    [1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
]
# values = [
#     [1, 1, 1],
#     [0, 0, 1],
#     [0, 1, 1],
#     [1, 1, 1],
# ]

for value in values:
    print("Значение для входа:", value, " = ", network.calculate__result(value))














