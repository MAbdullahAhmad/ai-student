import numpy as np
import pandas as pd

def drop_column(data, col):
  """
  drop_column(data, col)

  ```py
  # Example usage:

  # For Pandas DataFrame
  df = pd.DataFrame({
      'A': [1, 2, 3],
      'B': [4, 5, 6],
      'C': [7, 8, 9]
  })
  drop_column(df, 'B')

  # For NumPy array
  arr = np.array([
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ])
  drop_column(arr, 1)

  # For list of lists
  lst = [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ]
  drop_column(lst, 1)
  ```
  """


  if isinstance(data, pd.DataFrame):
    if col in data.columns: return data.drop(columns=[col])
    else: raise ValueError("Column not found in DataFrame")
  
  elif isinstance(data, np.ndarray):
    if col < data.shape[1]: return np.delete(data, col, axis=1)
    else: raise IndexError("Column index out of bounds for NumPy array")
  
  elif isinstance(data, list):
    if all(len(row) > col for row in data): return [row[:col] + row[col+1:] for row in data]
    else: raise IndexError("Column index out of bounds for list of lists")
  
  else: raise TypeError("Unsupported data type")

