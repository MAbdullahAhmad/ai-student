from .show import show as s

from .configure import configure_graph

def draw_scatter(p=None, x=[], y=None, show=False):
  """
  draw scatter plot

  ```py
  # Example usage:
  x = [1, 2, 3, 4, 5]
  y = [2, 3, 5, 4, 6]

  draw_scatter(plt, x, y, show=True)
  ```
  """

  p = p or configure_graph()
  y = y or list(range(len(x)))

  p.scatter(x, y)
  if show: s(p)

  return p