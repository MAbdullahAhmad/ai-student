import numpy as np
from collections.abc import Iterable
from numbers import Number

from ....core.interfaces.Model import Model
from ....core.functions.mean import simple_mean as mean


class MultilinearRegressor(Model):
  """
  MultilinearRegressor

  performs regression on multiple variables.

  ```
  # Example data
  X = [[1, 2], [2, 3], [3, 4], [4, 5]]
  y = [2, 4, 5, 4]

  # Initialize and fit the model
  model = MultilinearRegressor()
  model.fit(X, y)

  # Make predictions
  X_new = [[1, 2], [2, 3], [3, 4]]
  predictions = model.predict(X_new)

  print(f"Weights: {model.weights}")
  print(f"Predictions: {predictions}")
  ```
  """

  def __init__(self):
    self.weights = None

    self.intercept = 0
    self.coefficients = []


  def train(self, X: Iterable[Iterable[Number]], Y: Iterable[Number]):
    """
    Train the multilinear regression model to the data.
    
    Parameters:
    X: list of list of shape (n_samples, n_features)
    Y: list of shape (n_samples,)
    """
    X = np.array(X)
    Y = np.array(Y)
    
    # Add a column of ones to X for the intercept term
    X = np.hstack([np.ones((X.shape[0], 1)), X])
    
    # Compute weights using the Normal Equation: (X^T * X)^-1 * X^T * Y
    X_transpose = X.T
    self.weights = np.linalg.inv(X_transpose @ X) @ X_transpose @ Y

    self.intercept, self.coefficients = self.weights[0], self.weights[1:]


  def test(self, X):
    """
    Predict using the multilinear model.
    
    Parameters:
    X: list of list of shape (n_samples, n_features)
    
    Returns:
    y_pred: list of shape (n_samples,)
    """
    X = np.array(X)
    
    # Add a column of ones to X for the intercept term
    X = np.hstack([np.ones((X.shape[0], 1)), X])
    
    return X @ self.weights

