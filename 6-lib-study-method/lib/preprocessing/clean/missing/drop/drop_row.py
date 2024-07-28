import numpy as np
import pandas as pd

def drop_row(data, row):
  """
  drop_row(data, row)
  
  ```py
  # Example usage:

  # For Pandas DataFrame
  df = pd.DataFrame({
      'A': [1, 2, 3],
      'B': [4, 5, 6],
      'C': [7, 8, 9]
  })
  drop_row(df, 1)

  # For NumPy array
  arr = np.array([
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ])
  drop_row(arr, 1)

  # For list of lists
  lst = [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ]
  drop_row(lst, 1)
  ```
  """

  
  if isinstance(data, pd.DataFrame):
    if 0 <= row < len(data): return data.drop(index=row)
    else: raise IndexError("Row index out of bounds for DataFrame")

  elif isinstance(data, np.ndarray):
    if 0 <= row < data.shape[0]: return np.delete(data, row, axis=0)
    else: raise IndexError("Row index out of bounds for NumPy array")
  
  elif isinstance(data, list):
    if 0 <= row < len(data): return [r for i, r in enumerate(data) if i != row]
    else: raise IndexError("Row index out of bounds for list of lists")
  
  else: raise TypeError("Unsupported data type")

