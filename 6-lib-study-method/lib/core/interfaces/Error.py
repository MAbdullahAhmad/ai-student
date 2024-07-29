from abc import ABC, abstractmethod

class Erorr(ABC):
  """
  Model class

  Required Methods:
  - calculate

  Optional Methods
  - derivative

  """

  @abstractmethod
  def calculate(self, *args, **kwargs): pass
  