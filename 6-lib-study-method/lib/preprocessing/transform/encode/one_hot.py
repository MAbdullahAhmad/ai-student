import pandas as pd
import numpy as np
from collections.abc import Callable, Iterable

def one_hot(data, target, return_as='list'):
  """
  one_hot(data, target, return_as)

  One Hot Encoding
  """

  
  if isinstance(data, pd.DataFrame):
    encoded = pd.get_dummies(data, columns=target if isinstance(target, Iterable) else ([target] if target is not None else target))
    if return_as == 'list': return encoded.values.tolist()
    elif return_as == 'np': return encoded.values
    elif return_as == 'pd': return encoded

  elif isinstance(data, np.ndarray):
    return one_hot(data.tolist(), target, return_as)

  elif isinstance(data, list):
    target = target if isinstance(target, Iterable) else [target]
    unique_values = {col: sorted(set(row[col] for row in data)) for col in target}


    encoded = []
    for row in data:
      encoded_row = []
      for i, val in enumerate(row):
        if i in unique_values:
          encoded_row += [1 if val == u else 0 for u in unique_values[i]]
        else: encoded_row.append(val)
      encoded.append(encoded_row)

    if return_as == 'list': return encoded
    elif return_as == 'np': return np.array(encoded)
    elif return_as == 'pd': return pd.DataFrame(encoded)

  else: raise TypeError("Input data must be a pandas DataFrame, numpy array, or list.")

