import numpy as np
from ..core.Activation import Activation


#
# Tanh activation
#

class Tanh():

  def apply(self, x):
    return np.tanh(x)
  
  def apply_derivative(self, x):
    return 1 - self.apply(x) ** 2