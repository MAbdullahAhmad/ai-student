# 
# Imports
# 

import numpy as np
from collections.abc import Iterable
from numbers import Number

from ..core.Layer import Layer as LayerInterface
from ..core.Activation import Activation

from ..neuron.Neuron import Neuron
from ..activation.Sigmoid import Sigmoid



# 
# Layer
# 

class Layer(LayerInterface):

  
  # constructor
  def __init__(self, count:int, input_size:int, activation:str|Activation=None):
    activation = activation or Sigmoid()

    self.neurons = [
      Neuron(
        input_size=input_size,
        activation=activation
      ) for _ in range(count)
    ]

  
  # forward
  def forward(self, inputs:Iterable):
    outputs = np.array([neuron.forward(inputs) for neuron in self.neurons])
    return outputs

  
  # backward
  def backward(self, errors:Iterable, learning_rate:Number):
    next_errors = np.zeros(len(self.neurons[0].weights))
    
    for i, neuron in enumerate(self.neurons):
      next_errors += neuron.backward(error=errors[i], learning_rate=learning_rate)
    
    return next_errors
  