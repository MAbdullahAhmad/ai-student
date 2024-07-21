import numpy as np
from ..core.Loss import Loss


#
# Custom Exceptions
#

class InvalidReduction(Exception): pass



#
# Mean Absolute Error
#

class BinaryCrossentropy(Loss):


  def __init__(self, epilon:float=1e-15, reduction:str='mean'):
    """
      epilon: to clip y_pred
      reduction: either 'mean' or 'sum'
    """

    if reduction != 'mean' and reduction != 'sum':
      raise InvalidReduction(f'reduction must be either "mean" or "sum" found "{reduction}"')

    self.epilon = epilon
    self.reduction = reduction


  def calculate(self, y_true, y_pred):
    y_pred = np.clip(y_pred, self.epilon, 1-self.epilon)

    tmp = y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
    return -(
      np.mean(tmp) if self.reduction == 'mean' else np.sum(tmp)
    )