from ..core.interfaces.Activation import Activation


#
# ReLu activation
#

class Threshold(Activation):
  def __init__(self, threshold=0.5):
    self.threshold = threshold

  def apply(self, x):
    return 0 if x < self.threshold else 1