

from vendor.network.Network import Network


class WithTeacherNetwork(Network):

    def __init__(self, config=[], teacher=[]):
        super().__init__(layers=config)
        self.teacher = teacher
        self.current__teacher_index = 0
        self.learning__rate = .6
        self.learning__ages = 15000
        self.weights__delta = None

    def training(self):
        i = 0
        while i < self.learning__ages:
            for teacher__index in range(0, len(self.teacher)):
                self.set_current_teacher(teacher__index)
                self.forward__distribution()
                self.back__distribution()
                self.weights__delta = None
                self.get__result()
            i += 1

    def forward__distribution(self):
        for layer in self.layers:
            neurons = layer.get__neurons()
            for neuron in neurons:
                neuron.calculate__weight()

    def set__values(self, values=[]):
        layer = self.get__layer(0)
        layer.set__layer_values(values)

    def calculate__result(self, values=[]):
        self.set__values(values=values)
        self.forward__distribution()
        last__layer = self.get__layer(len(self.layers)-1)
        neurons = last__layer.get__neurons()

        arr = []
        for neuron in neurons:
            arr.append(neuron.value)
        return arr

    def get__result(self):
        layer = self.get__layer(len(self.layers)-1)
        neurons = layer.get__neurons()
        arr = []
        for neuron in neurons:
            arr.append(neuron.value)
        print("При учителе: ", self.teacher[self.current__teacher_index])
        print("Значение нейронов = ", arr)

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
        neurons = last__layer.get__neurons()
        i = 0
        for neuron in neurons:
            expected_value = self.teacher[self.current__teacher_index][1][i]
            neuron.error = neuron.value - expected_value
            # print("Ошибка нейрона ", i, " = ", neuron.error)
            # print("Значение нейрона ", i, " = ", neuron.value)
            # print("Значение учителя = ", self.teacher[self.current__teacher_index][1][i])
            i += 1

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

        for layer in reversed(self.layers):
            for neuron in layer.get__neurons():

                self.weights__delta = neuron.error * neuron.sigmoid_dx()

                for reverse in neuron.get__reverse_bounded():

                    reverse__same = self.get__same_neuron(neuron, reverse['neuron'].get_bounded())
                    reverse__value = reverse['neuron'].value
                    reverse__same['weight'] = reverse__same['weight'] - reverse__value * self.weights__delta * self.learning__rate
                    reverse['neuron'].error = reverse__same['weight'] * self.weights__delta

    # def back__distribution(self):
    #
    #     self.calculate__error()
    #     i = 0
    #     for layer in reversed(self.layers):
    #         for neuron in layer.get__neurons():
    #
    #             if i == 0:
    #                 self.weights__delta = neuron.error * neuron.sigmoid_dx()
    #
    #             for reverse in neuron.get__reverse_bounded():
    #
    #                 if i > 0:
    #                     self.weights__delta = neuron.error * neuron.sigmoid_dx()
    #
    #                 reverse__same = self.get__same_neuron(neuron, reverse['neuron'].get_bounded())
    #                 reverse__value = reverse['neuron'].value
    #                 reverse__same['weight'] = reverse__same['weight'] - reverse__value * self.weights__delta * self.learning__rate
    #                 reverse__same['neuron'].error = reverse__same['weight'] * self.weights__delta
    #         i += 1

















