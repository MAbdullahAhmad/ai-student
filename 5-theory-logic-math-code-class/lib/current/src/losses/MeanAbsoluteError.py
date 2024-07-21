import numpy as np
from ..core.Loss import Loss


#
# Mean Absolute Error
#

class MeanAbsoluteError(Loss):

  def calculate(self, y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))