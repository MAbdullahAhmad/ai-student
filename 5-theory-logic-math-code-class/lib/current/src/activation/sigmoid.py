import numpy as np

# Sigmoid function
def sigmoid(x):
  return 1 / (1 + np.exp(-x))