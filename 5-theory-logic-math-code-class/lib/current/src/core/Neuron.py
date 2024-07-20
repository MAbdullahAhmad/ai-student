from abc import ABC, abstractmethod

class Neuron(ABC):
  """
  Neuron class

  Required Props:
  - learning_rate
  
  Optional Props:
  - activation_function
  - optimizer
  - loss_method

  Required Methods:
  - train
  - predict
  - test
  - forward (returns predicted and error)
  - backward (returns updated weights)
  
  Optional Methods
  - activation
  - optimize
  - calculate_loss
  """


  @abstractmethod
  def train(self, *args, **kwargs): pass

  @abstractmethod
  def predict(self, x): pass

  @abstractmethod
  def test(self, *args, **kwargs): pass

  @abstractmethod
  def forward(self, x, y): pass

  @abstractmethod
  def backward(self, error, x): pass
  