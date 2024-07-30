import numpy as np
from ..core.interfaces.Activation import Activation


#
# Tanh activation
#

class Tanh(Activation):

  def apply(self, x):
    return np.tanh(x)
  
  def derivative(self, x):
    return 1 - self.apply(x) ** 2