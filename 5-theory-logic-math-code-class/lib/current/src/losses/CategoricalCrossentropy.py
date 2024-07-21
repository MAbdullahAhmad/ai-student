import numpy as np
from ..core.Loss import Loss


#
# Mean Absolute Error
#

class CategoricalCrossentropy(Loss):


  def __init__(self, epilon:float=1e-15):
    """
      epilon: to clip y_pred
    """
    self.epilon = epilon


  def calculate(self, y_true, y_pred):
    y_pred = np.clip(y_pred, self.epilon, 1-self.epilon)
    return -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]