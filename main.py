import sys
import numpy as np
import matplotlib

inputs = [1, 2]
weights = [[1, 2], [3, 4], [5, 6]]
biases = [1, 2, 3]
output = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for weight, n_input in zip (neuron_weights, inputs):
        neuron_output += weight * n_input
    neuron_output += neuron_bias
    output.append(neuron_output)
