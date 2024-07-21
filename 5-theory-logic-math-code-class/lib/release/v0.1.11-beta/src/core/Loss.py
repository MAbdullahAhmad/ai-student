from abc import ABC, abstractmethod

class Loss(ABC):
  """
  Loss class

  Required Methods:
  - calculate
  - derivative
  """


  @abstractmethod
  def calculate(self, y_true, y_pred): pass

  @abstractmethod
  def derivative(self, *args, **kwargs): pass
