from vendor.network.Network import Network


class WithTeacherNetwork(Network):

    def __init__(self, config=[], teacher=[]):
        super().__init__(layers=config)
        self.teacher = teacher
        self.current__teacher_index = 0
        self.learning__rate = 0.05
        self.learning__ages = 1
        self.weights__delta = None

    def training(self):
        i = 0
        while i < self.learning__ages:
            for teacher__index in range(0, len(self.teacher)):
                self.set_current_teacher(teacher__index)
                print("Текущий учитель: ", self.teacher[self.current__teacher_index])
                self.forward__distribution()
                self.get__result()
                self.back__distribution()
                # print("Дельта весов: ", self.weights__delta)
                self.weights__delta = None
                print("_______________")
                # self.get__weights()
            i += 1

    def forward__distribution(self):
        for layer in self.layers:
            neurons = layer.get__neurons()
            for neuron in neurons:
                neuron.calculate__weight()

    def get__result(self):
        layer = self.get__layer(len(self.layers)-1)
        neuron = layer.get__neuron(0)
        print("Значение нейрона: ", neuron.value)

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
        print("Значение ошибки: ", neuron.error)

    def get__weights(self):
        i = 1
        for layer in self.layers:
            print("Слой номер ____ ", i)
            for neuron in layer.get__neurons():
                print("________нейрон_________")
                print(neuron.value)
                print(neuron.bounded)
                for bound in neuron.bounded:
                    print(bound['weight'])
                print("_______________________")
            i += 1


    def back__distribution(self):
        self.calculate__error()
        i = 0
        for layer in reversed(self.layers):
            for neuron in layer.get__neurons():
                # print("Ошибка нейрона: ", neuron.error)
                self.weights__delta = neuron.error * neuron.sigmoid_dx()

                for reverse in neuron.get__reverse_bounded():
                    reverse__same = self.get__same_neuron(neuron, reverse['neuron'].get_bounded())
                    reverse__value = reverse['neuron'].value
                    # print("Значение весов_______________")
                    # print(reverse['weight'])
                    reverse__same['weight'] = reverse__same['weight'] - reverse__value * self.weights__delta * self.learning__rate
                    reverse['neuron'].error = reverse__same['weight'] * self.weights__delta

                    # print("Ошибка нейрона_______________")
                    # print(reverse['neuron'].error)
                    # print("_______________Ошибка нейрона")
                    # print(reverse['weight'])
                    # print("______________Значение весов")
                i += 1

















