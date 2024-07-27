from abc import ABC, abstractmethod

class Activation(ABC):
  """
  Activation class

  Required Methods:
  - apply
  - apply_derivative
  """


  @abstractmethod
  def apply(self, x): pass

  @abstractmethod
  def derivative(self, x): pass
  