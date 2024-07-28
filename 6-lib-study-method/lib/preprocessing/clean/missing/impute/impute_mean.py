import numpy as np
import pandas as pd

def impute_mean(data, col):
  """
  impute_mean(data, col)
  
  fill missing values by mean
  """


  if isinstance(data, pd.DataFrame):
    if col in data.columns and data[col].dtype in [np.float64, np.int64]:
      mean_value = data[col].mean()
      return data.fillna({col: mean_value})
    else: raise ValueError("Column not found or not numerical in DataFrame")

  elif isinstance(data, np.ndarray):
    if 0 <= col < data.shape[1]:
      col_data = data[:, col]
      mean_value = np.nanmean(col_data)
      col_data[np.isnan(col_data)] = mean_value
      return data
    else: raise IndexError("Column index out of bounds for NumPy array")

  elif isinstance(data, list):
    if all(len(row) > col for row in data):
      col_data = [row[col] for row in data if row[col] is not None]
      mean_value = np.nanmean(col_data)
      return [[mean_value if v is None else v for v in row] for row in data]
    else: raise IndexError("Column index out of bounds for list of lists")
  
  else: raise TypeError("Unsupported data type")

