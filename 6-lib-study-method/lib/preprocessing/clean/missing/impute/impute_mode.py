import numpy as np
import pandas as pd

def impute_mode(data, col):
  """
  impute_mode(data, col)

  Fill missing values by mode
  """


  if isinstance(data, pd.DataFrame):
    if col in data.columns and data[col].dtype in [np.float64, np.int64]:
      mode_value = data[col].mode()[0]
      return data.fillna({col: mode_value})
    else: raise ValueError("Column not found or not numerical in DataFrame")

  elif isinstance(data, np.ndarray):
    if 0 <= col < data.shape[1]:
      col_data = data[:, col]
      mode_value = pd.Series(col_data).mode()[0]
      col_data[np.isnan(col_data)] = mode_value
      return data
    else: raise IndexError("Column index out of bounds for NumPy array")

  elif isinstance(data, list):
    if all(len(row) > col for row in data):
      col_data = [row[col] for row in data if row[col] is not None]
      mode_value = pd.Series(col_data).mode()[0]
      return [[mode_value if v is None else v for v in row] for row in data]
    else: raise IndexError("Column index out of bounds for list of lists")

  else: raise TypeError("Unsupported data type")

