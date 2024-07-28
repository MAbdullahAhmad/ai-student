from .select_columns import select_columns

def split_io(data, output_col, return_as='list'):
  return (
    select_columns(data, output_col, return_as, True),
    select_columns(data, output_col, return_as, False)
  )