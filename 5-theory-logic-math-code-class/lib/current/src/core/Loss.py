from abc import ABC, abstractmethod

class Loss(ABC):
  """
  Loss class

  Required Methods:
  - calculate
  """


  @abstractmethod
  def calculate(self, y_true, y_pred): pass
