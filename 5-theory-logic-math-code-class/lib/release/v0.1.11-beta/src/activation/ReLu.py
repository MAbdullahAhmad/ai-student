from ..core.Activation import Activation


#
# ReLu activation
#

class ReLu(Activation):

  def apply(self, x):
    return max(0, x)
  
  def derivative(self, x):
    return 1 if x > 0 else 0