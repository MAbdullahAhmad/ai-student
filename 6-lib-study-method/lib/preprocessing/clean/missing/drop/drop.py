from .drop_column import drop_column
from .drop_row import drop_row

def drop(data, id, axis):
  """
  drop(data, id, axis)

  ```
  # Example usage:

  # For Pandas DataFrame
  df = pd.DataFrame({
      'A': [1, 2, 3],
      'B': [4, 5, 6],
      'C': [7, 8, 9]
  })
  print(drop(df, 1, axis=0))  # Drop row 1
  print(drop(df, 'B', axis=1))  # Drop column 'B'

  # For NumPy array
  arr = np.array([
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ])
  print(drop(arr, 1, axis=0))  # Drop row 1
  print(drop(arr, 1, axis=1))  # Drop column 1

  # For list of lists
  lst = [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ]
  ```
  """


  print(drop(lst, 1, axis=0))  # Drop row 1
  print(drop(lst, 1, axis=1))  # Drop column 1
  if axis == 0: return drop_row(data, id)
  elif axis == 1: return drop_column(data, id)
  else: raise ValueError("Axis must be 0 (row) or 1 (column)")

