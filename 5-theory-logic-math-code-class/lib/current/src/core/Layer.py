from abc import ABC, abstractmethod

class Layer(ABC):
  """
  Layer class

  Required Methods:
  - forward
  - backward
  """


  @abstractmethod
  def forward(self, *args, **kwargs): pass

  @abstractmethod
  def backward(self, *args, **kwargs): pass
  