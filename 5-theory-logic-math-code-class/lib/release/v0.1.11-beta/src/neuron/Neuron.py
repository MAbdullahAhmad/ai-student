#
# Imports
#

import numpy as np
from collections.abc import Iterable
from numbers import Number

from ..core.Neuron     import Neuron
from ..core.Activation import Activation
from ..core.Loss       import Loss
from ..core.Optimizer  import Optimizer

from ..activation.Sigmoid import Sigmoid
from ..activation.ReLu    import ReLu
from ..activation.Tanh    import Tanh

from ..losses.MeanSquaredError        import MeanSquaredError
from ..losses.MeanAbsoluteError       import MeanAbsoluteError
from ..losses.BinaryCrossentropy      import BinaryCrossentropy
from ..losses.CategoricalCrossentropy import CategoricalCrossentropy
from ..losses.Hinge                   import Hinge

from ..optimizers.StochasticGradientDescent import StochasticGradientDescent




#
# Customer Exceptions
#

class InvalidInitialWeights(Exception): pass

class UnexpectedInputsShape(Exception): pass
class UnexpectedOutputsShape(Exception): pass

class InvalidActivation(Exception): pass
class InvalidOptimizer(Exception): pass
class InvalidLoss(Exception): pass



class Neuron(Neuron):

  # 
  # Props
  # 

  builtin:dict = {
    'activation': {
      'default': Sigmoid,
      'sigmoid': Sigmoid,
      'relu': ReLu,
      'tanh': Tanh,
    },
    'loss_function': {
      'default': MeanSquaredError,
      'mse': MeanSquaredError,
      'mae': MeanAbsoluteError,
      'bce': BinaryCrossentropy,
      'cce': CategoricalCrossentropy,
      'hinge': Hinge,
    },
    'optimizer': {
      'default': StochasticGradientDescent,
      'sgd': StochasticGradientDescent,
    }
  }

  core:dict = {
    'activation':    Activation,
    'loss_function': Loss,
    'optimizer':     Optimizer,
  }

  errors:dict = {
    'activation':    InvalidActivation,
    'loss_function': InvalidLoss,
    'optimizer':     InvalidOptimizer,
  }

  input:Iterable = []
  output:float = 0.0

  delta:float = 0.0


  weight_gradient:Iterable = []
  bias_gradient:float = 0.0



  # 
  # Constructor
  # 

  def __init__(
      self,

      input_size:int,
      
      learning_rate:float=0.1,
      activation:str|Activation='default',
      loss_function:str|Loss='default',
      optimizer:str|Optimizer='default',

      initial_weights:Number|Iterable=0,
      initial_bias:Number=0,
    ):

    #> input size and learning rate

    # Input Size
    self.input_size = input_size
    self.input = np.repeat(0, self.input_size)
    
    # Learning Rate
    self.learning_rate = learning_rate

    #> activation, loss_function and optimizer

    params = {
      'activation':    activation,
      'loss_function': loss_function,
      'optimizer':     optimizer,
    }

    # iterate all
    for target in ['activation', 'loss_function', 'optimizer']:

      # get param
      param = params[target]
      

      # if present in builtin, set
      if type(param) == str and param in self.builtin[target].keys():
        setattr(self, target, self.builtin[target][param]())

      # if object, set directly
      elif isinstance(param, self.core[target]): setattr(self, target, param)
      
      # raise error
      # if not in {object, str} or string and not in builtin
      else: raise self.errors[target](param)


    #> Initial Weights & Bias

    # initial weights
    if isinstance(initial_weights, Number):                                            self.weights = np.repeat(initial_weights, input_size).astype(float)
    elif isinstance(initial_weights, Iterable) and len(initial_weights) == input_size: self.weights = np.array(initial_weights).astype(float)
    else: raise InvalidInitialWeights(f'Value must be either a number or an Iterable of size {input_size}')

    # initialize gradient to zero
    self.weight_gradient = np.repeat(0.0, self.input_size)

    # initial bias
    self.bias = initial_bias


  
  #
  # Forward
  #

  def forward(self, input):
    self.input = np.array(input)

    # if 1d, predict
    if len(self.input.shape) and self.input.shape[0] == self.input_size:
      # weighted sum
      weighted_sum = np.dot(self.input, self.weights) + self.bias

      # activation
      self.output = self.activation.apply(weighted_sum)

      # return
      return self.output
    
    # elif 2d, predict multiple
    return self.forward_multiple(self.input)



  #
  # Forward Multiple samples
  #

  def forward_multiple(self, inputs):
    inputs = np.array(inputs)

    if len(inputs.shape) < 2 or inputs.shape[1] != self.input_size:
      raise UnexpectedInputsShape(f'Inputs shape must be (n, {self.input_size}). found {inputs.shape}')

    results = []
    for inp in inputs:
      results.append(self.forward(inp))

    return np.array(results)



  #
  # Backward Pass (loss & optimize)
  #

  def backward(self, error=None):
    self.error = error or self.error

    # gradient
    self.delta = self.error * self.activation.derivative(self.output)

    # return loss for previous neurons
    return np.dot(self.delta, self.weights)



  #
  # Train
  #

  def train(self, inputs:Iterable, outputs:Iterable, epochs:int=100, batch_size:int=None, verbose:int=1):
    inputs = np.array(inputs)
    outputs = np.array(outputs)

    if len(inputs.shape) < 2 or inputs.shape[1] != self.input_size:    raise UnexpectedInputsShape (f'Inputs shape must be (n, {self.input_size}). found {inputs.shape}')
    if len(outputs.shape) != 1 or outputs.shape[0] != inputs.shape[0]: raise UnexpectedOutputsShape(f'Outputs size ({outputs.shape[0]}) differs from no of samples in input ({inputs.shape[0]})')

    # batch size: set counter
    if batch_size:
      self.batch_size = batch_size
      self.batch_counter = 0

    # batch reset
    def reset_batch(): self.predicted = []

    # batch end
    def batch_end():
      self.loss = self.loss_function.calculate(outputs, self.predicted)
      if verbose: print(f'epoch={e+1}, loss={self.loss}, samples={len(self.predicted)}')

    reset_batch()

    # main loop
    for e in range(epochs):
      
      if not batch_size: reset_batch()
      
      for i in range(outputs.shape[0]):

        # Forward Pass
        self.forward(inputs[i])
        self.predicted.append(self.output)

        # error calculation
        self.error = self.output - outputs[i]

        # Backward Pass
        self.backward()

        # Weights Updation
        if self.optimizer.mode == self.optimizer.MODES['SAMPLE']:
          self.optimizer.update(self)

        if verbose > 1: print(f'epoch={e+1}, sample={i+1}, actual={outputs[i]}, predicted={self.output}, error={self.error}')
      
        # batch logic
        if batch_size:
          self.batch_counter += 1
          if self.batch_counter >= self.batch_size:
            batch_end()

            if self.optimizer.mode == self.optimizer.MODES['BATCH']:
              self.optimizer.update(self)

            self.batch_counter = 0
            reset_batch()

      # epoch end (if batch_size=None)
      if not batch_size: batch_end()
    
    if batch_size and len(self.predicted):
      batch_end()



  #
  # Test
  #

  def test(self, inputs:Iterable, outputs:Iterable, verbose:int=0, binary:bool=True):
    inputs = np.array(inputs)
    outputs = np.array(outputs)

    if len(inputs.shape) < 2 or inputs.shape[1] != self.input_size:    raise UnexpectedInputsShape (f'Inputs shape must be (n, {self.input_size}). found {inputs.shape}')
    if len(outputs.shape) != 1 or outputs.shape[0] != inputs.shape[0]: raise UnexpectedOutputsShape(f'Outputs size ({outputs.shape[0]}) differs from no of samples in input ({inputs.shape[0]})')
    

    accurate = 0
    wrong    = 0
    for i in range(inputs.shape[0]):

      # Forward Pass
      predicted = self.forward(inputs[i])
      if binary: predicted = int(round(predicted))

      if predicted == outputs[i]: accurate+=1
      else:                       wrong   +=1

      if verbose > 1: print(f'sample={i+1}, predicted={predicted}, actual={outputs[i]}, error={outputs[i] - predicted}')

    return {
      'total':    accurate + wrong,
      'accurate': accurate,
      'wrong':    wrong,
    }
