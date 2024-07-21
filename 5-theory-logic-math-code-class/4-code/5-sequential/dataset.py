import numpy as np

# Dataset: [
# - Door 1
# - Door 2,
# - Door 3
# - Light
# ]
data = np.array([
  [1, 1, 1, 1],
  [0, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 0, 1, 0],
  [0, 1, 1, 0],
  [0, 0, 1, 0],
  [1, 1, 1, 1],
  [1, 1, 0, 1],
  [1, 1, 0, 1],
  [0, 0, 1, 0]
])

# Split inputs and outputs
X = data[:, 0:3]
Y = data[:, 3]