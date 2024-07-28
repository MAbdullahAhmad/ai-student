import numpy as np
import pandas as pd

def select_rows(data, indices, return_as='list', invert=False):
  """
  select_rows(data, indices, return_as)

  select specific rows only
  """


  if return_as not in ['list', 'np', 'pd']:
    raise ValueError("Invalid return_as value. Choose from 'list', 'np', 'pd'.")

  if isinstance(data, pd.DataFrame):
    selected = data.iloc[[i for i in data.index if i not in indices] if invert else indices]
    if return_as == 'list': return selected.values.tolist()
    elif return_as == 'np': return selected.values
    elif return_as == 'pd': return selected


  elif isinstance(data, np.ndarray):
    if isinstance(indices, list) and all(isinstance(i, int) for i in indices):
      selected = data[[i for i in range(data.shape[00]) if i not in indices] if invert else indices]
      if return_as == 'list': return selected.tolist()
      elif return_as == 'np': return selected
      elif return_as == 'pd': return pd.DataFrame(selected)
    else:
      raise ValueError("Indices must be a list of integers for NumPy array")

  elif isinstance(data, list):
    if isinstance(indices, list) and all(isinstance(i, int) for i in indices):
      selected = [[i for i in range(len(data)) if i not in indices] if invert else data[i] for i in indices]
      if return_as == 'list': return selected
      elif return_as == 'np': return np.array(selected)
      elif return_as == 'pd': return pd.DataFrame(selected)
    else:
      raise ValueError("Indices must be a list of integers for list of lists")

  else: raise TypeError("Unsupported data type")

