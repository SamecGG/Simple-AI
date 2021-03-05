import numpy as np

inputs = [1, 2]
weights = [[1, 2],
           [3, 4],
           [5, 6]]
biases = [1, 2, 3]

output = np.dot(weights, inputs) + biases
