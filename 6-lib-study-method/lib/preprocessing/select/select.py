from .select_rows    import select_rows
from .select_columns import select_columns

def select(data, indices_or_cols, axis=0, return_as='list', invert=False):
  """
  select columns or rows based on axis
  """


  if axis not in [0, 1]:
    raise ValueError("Invalid axis value. Choose 0 for rows or 1 for columns.")
  
  if axis == 0:   return select_rows   (data, indices_or_cols, return_as, invert)
  elif axis == 1: return select_columns(data, indices_or_cols, return_as, invert)
