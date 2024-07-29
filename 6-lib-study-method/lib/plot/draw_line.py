import numpy as np

from numbers import Number
from collections.abc import Iterable

from .show import show as s
from .configure import configure_graph

def draw_line(p=None, slope=0, intercept=0, range:Number|Iterable[Number]=[-1, 10], show=False):
  """
  draw a line on graph

  ```py
  # Example usage:
  slope = 0.9
  intercept = 1.3

  draw_line(plt, slope, intercept, show=True)
  ```
  """

  p = p or configure_graph()

  x = np.array([range] if isinstance(range, Number) else range)
  y = slope * x + intercept

  p.plot(x, y, color='red')
  if show: s(p)

  return p