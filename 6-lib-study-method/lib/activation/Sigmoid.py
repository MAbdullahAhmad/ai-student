import numpy as np
from ..core.interfaces.Activation import Activation


#
# Sigmoid activation
#

class Sigmoid(Activation):

  def apply(self, x):
    return 1 / (1 + np.exp(-x))
  
  def derivative(self, x):
    sig = self.apply(x)
    return sig * (1 - sig)