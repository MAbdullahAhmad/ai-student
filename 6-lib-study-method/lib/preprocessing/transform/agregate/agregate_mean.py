import pandas as pd
import numpy as np


def aggregate_mean(data, features, new_column_name: str = "aggregated_feature", return_as:str = "list"):
  """
  aggregate_mean(data, features, new_column_name, return_as)

  Aggregate features by creating one feature as the mean of many, and removing them.

  ```py
  # Example usage with pandas DataFrame with column names
  df = pd.DataFrame({
      'A': [1, 2, 3],
      'B': [4, 5, 6],
      'C': [7, 8, 9]
  })
  aggregate_mean(df, ['A', 'B'], 'mean_AB')

  # Example usage with pandas DataFrame with column indices
  df = pd.DataFrame({
      'A': [1, 2, 3],
      'B': [4, 5, 6],
      'C': [7, 8, 9]
  })
  aggregate_mean(df, [0, 1], 'mean_AB')

  # Example usage with numpy array
  np_array = np.array([
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ])
  aggregate_mean(np_array, [0, 1])

  # Example usage with 2d list
  lst = [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ]
  aggregate_mean(lst, [0, 1])
  ```
  """
    
  if isinstance(data, pd.DataFrame):
    if len(features):
      idx = type(features[0]) == int
      data[new_column_name] = (data.iloc[:, features] if idx else data[features]).sum(axis=1) / len(features)
      data.drop(data.columns[features] if idx else features, axis=1, inplace=True)

    if return_as == 'list': return data.values.tolist()
    elif return_as == 'np': return data.values
    elif return_as == 'pd': return data

  elif isinstance(data, np.ndarray):
    aggregated_feature = np.sum(data[:, features], axis=1, keepdims=True)
    data = np.delete(data, features, axis=1)
    data = np.hstack((data, aggregated_feature)) / len(features)

  elif isinstance(data, list):
    data = np.array(data)
    aggregated_feature = np.sum(data[:, features], axis=1, keepdims=True)
    data = np.delete(data, features, axis=1)
    data = np.hstack((data, aggregated_feature)) / len(features)

  else: raise TypeError("Unsupported data type. Please provide a pandas DataFrame, numpy array, or list of lists.")

  if return_as == 'list': return data.tolist()
  elif return_as == 'np': return data
  elif return_as == 'pd': return pd.DataFrame(data)
  
  