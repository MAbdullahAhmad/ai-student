import numpy as np
from ..core.Loss import Loss


#
# Mean Absolute Error
#

class Hinge(Loss):

  def calculate(self, y_true, y_pred):
    return np.mean(np.maximum(0, 1 - y_true * y_pred))