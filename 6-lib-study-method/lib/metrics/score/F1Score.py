import numpy as np
from ...core.interfaces.Score import Score

class F1Score(Score):
  """
  F1 Score

  ```py
  # Sample data
  y_true = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 0])
  y_pred = np.array([0, 1, 0, 0, 1, 1, 0, 1, 1, 0])

  # Instantiate the F1Score class
  f1_score = F1Score()

  # Calculate F1 score
  score = f1_score.calculate(y_true, y_pred)
  print(f"F1 Score: {score}")
  ```
  """
  def calculate(self, y_true, y_pred):
    return self.f1(
      self.precision(y_true, y_pred),
      self.recall(y_true, y_pred)
    )

  def precision(self, y_true, y_pred):
    true_positive = np.sum((y_true == 1) & (y_pred == 1))
    false_positive = np.sum((y_true == 0) & (y_pred == 1))
    return true_positive / (true_positive + false_positive)

  def recall(self, y_true, y_pred):
    true_positive = np.sum((y_true == 1) & (y_pred == 1))
    false_negative = np.sum((y_true == 1) & (y_pred == 0))
    return true_positive / (true_positive + false_negative)

  def f1(self, precision, recall):
    if precision + recall == 0: return 0
    return 2 * (precision * recall) / (precision + recall)

