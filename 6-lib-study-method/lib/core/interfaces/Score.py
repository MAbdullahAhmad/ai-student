from abc import ABC, abstractmethod

class Score(ABC):
  """
  Model class

  Required Methods:
  - calculate

  """

  @abstractmethod
  def calculate(self, *args, **kwargs): pass
  