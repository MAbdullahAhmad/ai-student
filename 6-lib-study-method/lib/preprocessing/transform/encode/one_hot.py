import pandas as pd
import numpy as np

def one_hot(data):
  if isinstance(data, pd.DataFrame):
    # Apply one-hot encoding to each column of the DataFrame
    return pd.get_dummies(data)

  elif isinstance(data, np.ndarray):
    # Convert numpy array to DataFrame and apply one-hot encoding
    df = pd.DataFrame(data, columns=['Feature'])
    return pd.get_dummies(df)

  elif isinstance(data, list):
    # Convert list to DataFrame and apply one-hot encoding
    df = pd.DataFrame(data, columns=['Feature'])
    return pd.get_dummies(df)

  else:
    raise TypeError("Input data must be a pandas DataFrame, numpy array, or list.")

# Example usage:

# For pandas DataFrame
df = pd.DataFrame({'Color': ['red', 'green', 'blue', 'green']})
encoded_df = one_hot(df)
print("Pandas DataFrame:\n", encoded_df)

# For numpy array
arr = np.array(['red', 'green', 'blue', 'green'])
encoded_arr = one_hot(arr)
print("\nNumpy Array:\n", encoded_arr)

# For list
lst = ['red', 'green', 'blue', 'green']
encoded_lst = one_hot(lst)
print("\nList:\n", encoded_lst)
