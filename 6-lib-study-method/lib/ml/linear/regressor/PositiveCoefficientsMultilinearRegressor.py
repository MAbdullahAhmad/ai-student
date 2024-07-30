import numpy as np
from collections.abc import Iterable
from numbers import Number
from scipy.optimize import nnls

from ....core.interfaces.Model import Model
from ....core.functions.mean import simple_mean as mean

class PositiveCoefficientsMultilinearRegressor(Model):
  """
  PositiveCoefficientsMultilinearRegressor

  performs regression on multiple variables with non-negative coefficients.

  ```
  # Example data
  X = [[1, 2], [2, 3], [3, 4], [4, 5]]
  y = [2, 4, 5, 4]

  # Initialize and fit the model
  model = PositiveCoefficientsMultilinearRegressor()
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
    Train the positive coefficients multilinear regression model to the data.
    
    Parameters:
    X: list of list of shape (n_samples, n_features)
    Y: list of shape (n_samples,)
    """
    X = np.array(X)
    Y = np.array(Y)
    
    # Add a column of ones to X for the intercept term
    X = np.hstack([np.ones((X.shape[0], 1)), X])
    
    # following solver makes intercept also positive only
    # # Compute weights using the NNLS solver
    # self.weights, _ = nnls(X, Y)
    # self.intercept, self.coefficients = self.weights[0], self.weights[1:]

    # Compute weights using the NNLS solver for coefficients
    self.coefficients, _ = nnls(X, Y)
    
    # Calculate intercept separately
    residuals = Y - X @ self.coefficients
    self.intercept = np.mean(residuals)


  def test(self, X):
    """
    Predict using the positive coefficients multilinear model.
    
    Parameters:
    X: list of list of shape (n_samples, n_features)
    
    Returns:
    y_pred: list of shape (n_samples,)
    """
    X = np.array(X)
    
    # Add a column of ones to X for the intercept term
    X = np.hstack([np.ones((X.shape[0], 1)), X])
    
    return X @ self.weights
