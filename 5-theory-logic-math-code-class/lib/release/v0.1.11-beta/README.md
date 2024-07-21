## Lib `v1.1.11-beta`

Under Development + Testing Library for Machine Learning.

## Directories in `src/`

Core:

- `src/core`: abstract classes / interfaces
  - `Neuron`: 
  - `Activation`: 
  - `Loss`: 
  - `Optimizer`: 

Reusables: 

- `src/activation`
  - `ReLu`: 
  - `Sigmoid`: 
  - `Tanh`: 

- `src/losses`
  - `MeanSquaredError`: 
  - `MeanAbsoluteError`: 
  - `BinaryCrossentropy`: 
  - `CategoricalCrossentropy`: 
  - `Hinge`: 

- `src/optimizers`
  - `StochasticGradientDescent`: 

Model Building:

- `src/neuron`:
  - `SimpleNeuron`: 
  - `Neuron`: 

## Examples

- `neuron`:
  - [`SimpleNeuron`](examples/neuron/1_simple_neuron.ipynb)
  - [`Neuron`](examples/neuron/2_neuron.ipynb)