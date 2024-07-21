# Lib `v1.2.1-beta`

Under Development + Testing Library for Machine Learning.

## Changelog

- __What's new in `v1.1`:__
  - Added `SimpleNeuron`
  - Added Trainable `Neuron`

- __What's new in `v1.2`:__
  - Introduced `Sequential` model

## Directories in `src/`

Core:

- `src/core`: abstract classes / interfaces
  - `Neuron`: 
  - `Activation`: 
  - `Loss`: 
  - `Optimizer`: 
  - `Layer`: 
  - `Sequential`: 

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

- `src/layers`:
  - `Layer`: 

- `src/sequential`:
  - `Sequential`: 

## Examples

- `neuron`:
  - [`SimpleNeuron`](examples/neuron/1_simple_neuron.ipynb)
  - [`Neuron`](examples/neuron/2_neuron.ipynb)

- `sequential`:
  - [`SimpleNeuron`](examples/neuron/1_simple_neuron.ipynb)
  - [`Neuron`](examples/neuron/2_neuron.ipynb)