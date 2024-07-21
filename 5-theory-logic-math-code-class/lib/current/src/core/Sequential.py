from abc import ABC, abstractmethod
from .Layer import Layer

class Sequential(ABC):
  """
  Sequential class

  Required Methods:
  - add
  - forward
  - backward
  - train
  """


  @abstractmethod
  def add(self, layer:Layer): pass

  @abstractmethod
  def forward(self, *args, **kwargs): pass

  @abstractmethod
  def backward(self, *args, **kwargs): pass

  @abstractmethod
  def train(self, *args, **kwargs): pass
  