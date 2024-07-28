import numpy as np
import pandas as pd

def impute_median(data, col):
  """
  impute_median(data, col)

  Fill missing values by median
  """

  if isinstance(data, pd.DataFrame):
    if col in data.columns and data[col].dtype in [np.float64, np.int64]:
      median_value = data[col].median()
      return data.fillna({col: median_value})
    else: raise ValueError("Column not found or not numerical in DataFrame")

  elif isinstance(data, np.ndarray):
    if 0 <= col < data.shape[1]:
      col_data = data[:, col]
      median_value = np.nanmedian(col_data)
      col_data[np.isnan(col_data)] = median_value
      return data
    else: raise IndexError("Column index out of bounds for NumPy array")

  elif isinstance(data, list):
    if all(len(row) > col for row in data):
      col_data = [row[col] for row in data if row[col] is not None]
      median_value = np.nanmedian(col_data)
      return [[median_value if v is None else v for v in row] for row in data]
    else: raise IndexError("Column index out of bounds for list of lists")
  
  else: raise TypeError("Unsupported data type")

