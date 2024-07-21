#
# Stochastic Gradient Descent
#

class StochasticGradientDescent():
  MODES = {
    'SAMPLE': 1,
    'BATCH': 2,
  }

  def __init__(self, learning_rate=None):
    self.learning_rate = learning_rate
    self.mode = self.MODES['SAMPLE']

  def update(self, model, learning_rate=0.01):
    # learning rate
    lr = self.learning_rate or model.learning_rate or learning_rate

    #> hierarchy functions
    
    # Neuron Level
    def update_neuron(neuron):
      neuron.weight_gradient = neuron.delta * neuron.input
      neuron.bias_gradient   = neuron.delta

      neuron.weights -= lr * neuron.weight_gradient
      neuron.bias    -= lr * neuron.bias_gradient

    # Layer Level
    def update_layer(layer):
      for neuron in layer.neurons: update_neuron(neuron, lr)

    # Network Level
    def update_network(model):
      for layer in model.layers: update_layer(layer, lr)

    # call
    if   hasattr(model, 'layers' ): update_network(model) # if ann
    elif hasattr(model, 'neurons'): update_layer  (model) # if layer
    elif hasattr(model, 'forward'): update_neuron (model) # if neuron

