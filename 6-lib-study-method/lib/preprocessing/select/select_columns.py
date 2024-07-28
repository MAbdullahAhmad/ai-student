import numpy as np
import pandas as pd


def select_columns(data, cols, return_as='list', invert=False):
  """
  select_columns(data, indices, return_as)

  select specific columns only
  """


  if return_as not in ['list', 'np', 'pd']:
    raise ValueError("Invalid return_as value. Choose from 'list', 'np', 'pd'.")

  if isinstance(data, pd.DataFrame):
    selected = data[[col for col in data.columns if col not in cols] if invert else cols]
    if return_as == 'list': return selected.values.tolist()
    elif return_as == 'np': return selected.values
    elif return_as == 'pd': return selected

  elif isinstance(data, np.ndarray):
    if isinstance(cols, list) and all(isinstance(c, int) for c in cols):
      selected = data[:, [c for c in data.columns if c not in cols] if invert else cols]
      if return_as == 'list': return selected.tolist()
      elif return_as == 'np': return selected
      elif return_as == 'pd': return pd.DataFrame(selected)
    else:
      raise ValueError("Columns must be a list of integers for NumPy array")

  elif isinstance(data, list):
    if all(isinstance(row, list) for row in data):
      selected = [[row[c] for c in ([c for c in range(len(data[0])) if c not in cols] if invert else cols)] for row in data]
      if return_as == 'list': return selected
      elif return_as == 'np': return np.array(selected)
      elif return_as == 'pd': return pd.DataFrame(selected)
    else:
      raise ValueError("Data must be a list of lists for list of lists")

  else: raise TypeError("Unsupported data type")

