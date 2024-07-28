import numpy as np
import pandas as pd

from .impute_constant import impute_constant
from .impute_mean     import impute_mean
from .impute_median   import impute_median
from .impute_mode     import impute_mode

def impute(data, col, method='mean', constant=None):
  """
  impute(data, col, method, constant)

  impute using mean, median, mode and constant
  (default mean)
  """
  
  if method not in ['mean', 'median', 'mode', 'constant']: raise ValueError("Invalid method. Choose from 'mean', 'median', 'mode', 'constant'.")
  if method == 'constant' and constant is None: raise ValueError("For 'constant' method, a 'constant' value must be provided.")
  if method != 'constant' and constant is not None: raise ValueError("The 'constant' parameter is only used with the 'constant' method.")

  if isinstance(data, pd.DataFrame):
    if data[col].dtype not in [np.float64, np.int64] and method not in ['constant', 'mode']: raise ValueError("Column must be numeric for methods other than 'constant' and 'mode'")
    
  elif isinstance(data, np.ndarray):
    if 0 <= col < data.shape[1]:
      if not np.issubdtype(data[:, col].dtype, np.number) or method not in ['constant', 'mode']:
        raise ValueError("Column must be numeric for methods other than 'constant'")
    else:
        raise IndexError("Column index out of bounds for NumPy array")

  elif isinstance(data, list):
    if all(len(row) > col for row in data):
      if method not in ['constant', 'mode'] or not all(v is not None for row in data for v in row[col] if v is not None):
        raise ValueError("Column must be numeric for methods other than 'constant'")
    else:
      raise IndexError("Column index out of bounds for data")

  if   method == 'mean':     return impute_mean    (data, col)
  elif method == 'median':   return impute_median  (data, col)
  elif method == 'mode':     return impute_mode    (data, col)
  elif method == 'constant': return impute_constant(data, col, constant)

  else: raise TypeError("Unsupported data type")

