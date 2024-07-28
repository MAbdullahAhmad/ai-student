import numpy as np
import pandas as pd

def impute_constant(data, col, constant):
  """
  impute_constant(data, col, constant)

  fill missing values by constant
  """


  if isinstance(data, pd.DataFrame):
    if col in data.columns: return data.fillna({col: constant})
    else: raise ValueError("Column not found in DataFrame")

  elif isinstance(data, np.ndarray):
    if 0 <= col < data.shape[1]:
      data[np.isnan(data[:, col]), col] = constant
      return data
    else: raise IndexError("Column index out of bounds for NumPy array")

  elif isinstance(data, list):
    if all(len(row) > col for row in data): return [[constant if v is None else v for v in row] for row in data]
    else: raise IndexError("Column index out of bounds for list of lists")
  
  else: raise TypeError("Unsupported data type")