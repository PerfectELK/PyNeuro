from vendor.network.Network import Network


class WithTeacherNetwork(Network):

    def __init__(self, config=[], teacher=[]):
        super().__init__(layers=config)
        self.teacher = teacher

    def training(self):
        for layer in self.layers:
            neurons = layer.get__neurons()
            print("Layer start")
            for neuron in neurons:
                neuron.calculate__weight()
                print(neuron.value)
            print("layer end")






