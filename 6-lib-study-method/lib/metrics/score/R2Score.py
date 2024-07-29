import numpy as np
from ...core.interfaces.Score import Score

class R2Score(Score):
  def calculate(self, y_true, y_pred):
    return 1 - (
      np.sum((y_true - y_pred) ** 2) / 
      np.sum((y_true - np.mean(y_true)) ** 2)
    )
