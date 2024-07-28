from abc import ABC, abstractmethod

class Model(ABC):
  """
  Model class

  Required Methods:
  - train
  - test

  """

  @abstractmethod
  def train(self, *args, **kwargs): pass

  @abstractmethod
  def test(self, error, x): pass
  