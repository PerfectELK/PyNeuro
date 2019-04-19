from vendor.layer.Layer import Layer

layer1 = Layer(3, begin__values=[1, 1, 0])
print("layer 1 created")
layer2 = Layer(4)
print("layer 2 created")
layer1.create_neurons()
print("layer 1 neurons created")
layer2.create_neurons()
print("layer 2 neurons created")

layer1.create_neighbours_layers(after_layer=layer2).bind_after_layer()
print("layer 1 bounded with 2 layer")
layer2.create_neighbours_layers(before_layer=layer1).bind_before_layer()
print("layer 2 bounded with 1 layer")

print(layer1.get__neurons()[0].value)





