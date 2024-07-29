from collections.abc import Iterable
from numbers import Number

from ....core.interfaces.Model import Model
from ....core.functions.mean import simple_mean as mean


class SimpleLinearRegressor(Model):
  """
  SimpleLinearRegressor

  performs regression on one variable.
  for multiple features, checkout 'LinearRegressor'

  ```
  # Example data
  X = [1, 2, 3, 4, 5]
  y = [2, 4, 5, 4, 5]

  # Initialize and fit the model
  model = LinearRegression()
  model.fit(X, y)

  # Make predictions
  X_new = [1, 2, 3, 4, 5]
  predictions = model.predict(X_new)

  print(f"Intercept: {model.intercept}")
  print(f"Slope: {model.slope}")
  print(f"Predictions: {predictions}")
  ```
  """


  def __init__(self):
    self.slope = 0
    self.intercept = 0


  def train(self, X: Iterable[Number], Y: Iterable[Number]):
    """
    Fit the linear regression model to the data.
    
    Parameters:
    X: list of shape (n_samples,)
    Y: list of shape (n_samples,)
    """


    # calcualte mean
    mX = mean(X)
    mY = mean(Y)

    # calculate slope
    self.slope = (
      sum((X[i] - mX) * (Y[i] - mY) for i in range(len(X)))
    ) / (
      sum((X[i] - mX) ** 2 for i in range(len(X)))
    )

    # calculate intercept
    self.intercept = mY - self.slope * mX


  def test(self, X):
    """
    Predict using the linear model.
    
    Parameters:
    X: list of shape (n_samples,)
    
    Returns:
    y_pred: list of shape (n_samples,)
    """
    return [self.intercept + self.slope * x for x in X]