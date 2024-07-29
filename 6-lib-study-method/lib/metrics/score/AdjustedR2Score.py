import numpy as np
from ...core.interfaces.Score import Score
from .R2Score import R2Score

class AdjustedR2Score(Score):
  def calculate(self, y_true, y_pred, n_predictors):
    n = len(y_true)
    return (
      1 - (
        1 - R2Score().calculate(y_true, y_pred)
      ) * (n - 1) / (n - n_predictors - 1)
    )
