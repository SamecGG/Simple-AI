import numpy as np

np.random.seed(0)

X = [[1, 2, 5, 0],
     [3, 2, 1, 3],
     [1, 3, -1, 2]]

class Dense_Layer:
     def __init__(self, n_inputs, n_neurons):
          self.weights = np.random.randn(n_inputs, n_neurons)
          self.biases = np.zeros(1, n_neurons)
     def forward(self, inputs):
          self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Dense_Layer(4, 5)
layer2 = Dense_Layer(5, 2)

layer1.forward(X)
layer2.forward(layer1.output)

layer2.output
