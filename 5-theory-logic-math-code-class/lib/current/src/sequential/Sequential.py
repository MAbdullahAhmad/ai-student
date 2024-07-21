# 
# Imports
# 

import numpy as np
from collections.abc import Iterable
from numbers import Number

from ..core.Sequential import Sequential as SequentialInterface
from ..core.Layer import Layer
from ..core.Loss import Loss

from ..losses.MeanSquaredError import MeanSquaredError

# 
# Sequential
# 

class Sequential(SequentialInterface):

  
  # constructor
  def __init__(self, layers:Iterable=None):
    self.layers = layers or []


  # add a layer
  def add(self, layer:Layer):
    self.layers.append(layer)


  # forward pass
  def forward(self, inputs:Iterable):
    for layer in self.layers:
      inputs = layer.forward(inputs)
    return inputs


  # backward pass
  def backward(self, error:Number|Iterable, learning_rate:Number):
    for layer in reversed(self.layers):
      error = layer.backward(error, learning_rate)


  # train
  def train(self, X:Iterable, Y:Iterable, epochs:int=100, loss_function:Loss=None, learning_rate:Number=0.01):
    loss_function = loss_function or MeanSquaredError()
    
    for _ in range(epochs):
      for i in range(len(X)):
        output = self.forward(X[i])
        error = loss_function.derivative(Y[i], output)
        self.backward(error, learning_rate)