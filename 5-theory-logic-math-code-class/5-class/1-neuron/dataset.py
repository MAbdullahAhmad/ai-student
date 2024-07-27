import numpy as np

# Dataset: [
# - Hours of study,
# - Classes attended,
# - Participation in study groups,
# - Pass/Fail
# ]
data = np.array([
  [10, 15, 1, 1],
  [5, 10, 0, 0],
  [8, 12, 1, 1],
  [3, 5, 0, 0],
  [7, 14, 1, 1],
  [4, 8, 0, 0],
  [9, 13, 1, 1],
  [2, 4, 0, 0],
  [6, 9, 0, 0],
  [11, 16, 1, 1]
])

# Split inputs and outputs
X = data[:, 0:3]
Y = data[:, 3]