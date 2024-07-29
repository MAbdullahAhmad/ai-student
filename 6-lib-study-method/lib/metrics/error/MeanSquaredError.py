import numpy as np
from ...core.interfaces.Error import Error


#
# Mean Squared Error
#

class MeanSquaredError(Error):

  def calculate(self, y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))
  
  def derivative(self, y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.size