import numpy as np
from ..core.Loss import Loss


#
# Mean Squared Error
#

class MeanSquaredError(Loss):

  def calculate(self, y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))