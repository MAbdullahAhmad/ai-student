from abc import ABC, abstractmethod

class Activation(ABC):
  """
  Activation class

  Required Methods:
  - apply

  Optional:
  - apply_derivative
  """


  @abstractmethod
  def apply(self, x): pass