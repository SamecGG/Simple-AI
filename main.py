import numpy as np

# 3 neurons => 3 outputs
inputs = [[1, 2],
          [3, 2]]

weights = [[1, 2],
           [3, 4],
           [5, 6]]

biases = [1, 2, 3]

weights2 = [[1, 2],
            [3, 4],
            [5, 6]]

biases2 = [1, 2, 3]

layer1_output = np.dot(inputs, np.array(weights).T) + biases
layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases

layer2_output
