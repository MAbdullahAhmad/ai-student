#
# imports
#

import numpy as np
from numbers import Number
from collections.abc import Iterable
from ..core.Neuron import Neuron


#
# custom exceptions
#

class InvalidInitialWeights(Exception): pass
class UnexpectedInputsShape(Exception): pass
class UnexpectedOutputsShape(Exception): pass


#
# SimpleNeuron class
#

class SimpleNeuron(Neuron):


  def __init__(self, input_size:int, learning_rate:float=0.1, initial_weights:Number|Iterable=0, initial_bias:Number=0):

    self.input_size = input_size
    
    if isinstance(initial_weights, Number):                                            self.weights = np.repeat(initial_weights, input_size)
    elif isinstance(initial_weights, Iterable) and len(initial_weights) == input_size: self.weights = np.array(initial_weights)
    else: raise InvalidInitialWeights(f'Value must be either a number or an Iterable of size {input_size}')

    self.bias = initial_bias

    self.learning_rate = learning_rate



  def activation(self, x:Iterable, threshold:float=0.2):
    return 1 if x > threshold else 0
  
  # forward
  def predict(self, x:Iterable):
    x = np.array(x)

    if len(x.shape) and x.shape[0] == self.input_size:
      # weighted sum
      weighted_sum = np.dot(x, self.weights) + self.bias

      # activation
      predicted = self.activation(weighted_sum)

      # return
      return predicted
    
    elif len(x.shape) > 1 and x.shape[1] == self.input_size:
      return self.predict_multiple(x)
    else: raise UnexpectedInputsShape(f'Inputs shape must be ({self.input_size}). found {x.shape}')
  


  def predict_multiple(self, inputs:Iterable):
    inputs = np.array(inputs)
    input_shape = inputs.shape

    if len(input_shape) < 2 or input_shape[1] != self.input_size:
      raise UnexpectedInputsShape(f'Inputs shape must be (n, {self.input_size}). found {input_shape}')

    results = []
    for i in range(input_shape[0]):
      results.append(inputs[i])

    return np.array(results)



  def forward(self, x:Iterable, y:Number):
    # predicted
    predicted = self.predict(x)

    # error
    error = y - predicted

    return predicted, error



  def backward(self, error:Number, x:Iterable):
    # update weights
    return (
      self.weights + self.learning_rate * error * x,
      self.bias + self.learning_rate * error
    )



  def train(self, inputs:Iterable, outputs:Iterable, epochs:int=100, verbose:int=1):
    inputs = np.array(inputs)
    outputs = np.array(outputs)
    input_shape = inputs.shape
    output_shape = outputs.shape

    if len(input_shape) < 2 or input_shape[1] != self.input_size:
      raise UnexpectedInputsShape(f'Inputs shape must be (n, {self.input_size}). found {input_shape}')
    if len(output_shape) != 1 or output_shape[0] != input_shape[0]:
      raise UnexpectedOutputsShape(f'Outputs size ({output_shape[0]}) differs from no of samples in input ({input_shape[0]})')
    
    for e in range(epochs):
      
      avg_err = 0
      
      for i in range(input_shape[0]):
        predicted, error = self.forward(inputs[i], outputs[i])
        self.weights, self.bias = self.backward(error, inputs[i])
        if verbose > 1: print(f'epoch={e+1}, sample={i+1}, error={error}')
        avg_err+=error

      avg_err /= input_shape[0]
      avg_err = round(avg_err, 2)
      
      if verbose: print(f'epoch={e+1}, error-avg={avg_err}')



  def test(self, inputs:Iterable, outputs:Iterable, verbose:int=0):
    inputs = np.array(inputs)
    outputs = np.array(outputs)
    input_shape = inputs.shape
    output_shape = outputs.shape

    if len(input_shape) < 2 or input_shape[1] != self.input_size:
      raise UnexpectedInputsShape(f'Inputs shape must be (n, {self.input_size}). found {input_shape}')
    if len(output_shape) != 1 or output_shape[0] != input_shape[0]:
      raise UnexpectedOutputsShape(f'Outputs size ({output_shape[0]}) differs from no of samples in input ({input_shape[0]})')
    

    accurate = 0
    wrong    = 0
    for i in range(input_shape[0]):
      predicted, error = self.forward(inputs[i], outputs[i])

      if predicted == outputs[i]: accurate+=1
      else:                       wrong+=1

      if verbose > 1: print(f'sample={i+1}, predicted={predicted}, actual={outputs[i]}, error={error}')

    return {
      'total': accurate + wrong,
      'accurate': accurate,
      'wrong': wrong,
    }