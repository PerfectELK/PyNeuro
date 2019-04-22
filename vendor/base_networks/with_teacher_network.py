from vendor.network.Network import Network


class WithTeacherNetwork(Network):

    def __init__(self, config=[], teacher=[]):
        super().__init__(layers=config)
        self.teacher = teacher
        self.current__teacher_index = 0
        self.learning__rate = 0.05
        self.weights__delta = None

    def training(self):
        for layer in self.layers:
            neurons = layer.get__neurons()
            print("Layer start")
            for neuron in neurons:
                neuron.calculate__weight()
                print(neuron.value)
            print("layer end")
        print("training end")
        self.back__distribution()

    def get__same_neuron(self, neuron, list):
        for n in list:
           if id(n['neuron']) == id(neuron):
               return n

    def set_current_teacher(self, index):
        layer = self.get__layer(0)
        layer.set__layer_values(self.teacher[index][0])
        self.current__teacher_index = index

    def calculate__error(self):
        last__layer = self.get__layer(len(self.layers)-1)
        neuron = last__layer.get__neuron(0)
        expected_value = self.teacher[self.current__teacher_index][1]
        neuron.error = neuron.value - expected_value

    def back__distribution(self):
        self.calculate__error()
        for layer in reversed(self.layers):
            for neuron in layer.get__neurons():
                if self.weights__delta is None:
                    self.weights__delta = neuron.error * neuron.sigmoid_dx()

                for reverse in neuron.get__reverse_bounded():
                    reverse__value = reverse['neuron'].value
                    reverse = self.get__same_neuron(neuron, reverse['neuron'].get_bounded())
                    reverse['weight'] = reverse['weight'] - reverse__value * self.weights__delta * self.learning__rate
                    reverse['neuron'].error = reverse['weight'] * self.weights__delta















