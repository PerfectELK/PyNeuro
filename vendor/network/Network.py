from vendor.layer.Layer import Layer


class Network:

    def __init__(self, layers=None):
        self.__layers = layers
        self.layers = []
        self.__create_layers()
        self.__bind__layers()

    def get__layer(self, index):
        return self.layers[index]

    def __create_layers(self):
        if self.__layers != None:
            for layer in self.__layers:
                layer_object = Layer(layer['amount_neurons'], layer['begin__values'])
                layer_object.create_neurons()
                self.layers.append(layer_object)

    def __bind__layers(self):
        if len(self.layers):
            for index in range(0, len(self.layers)):
                val = index
                current__layer = self.layers[index]
                try:
                    if(index-1 != -1):
                        current__layer.create_neighbours_layers(before_layer=self.layers[index-1]).bind_before_layer()
                except:
                    print()

                try:
                    current__layer.create_neighbours_layers(after_layer=self.layers[index+1]).bind_after_layer()
                except:
                    print()
