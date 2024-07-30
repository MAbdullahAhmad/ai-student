from collections.abc import Iterable

from .show import show as s
from .configure import configure_graph


def draw_circle(p=None, x=None, y=None, r=None, c='black', alpha=0.5, edge_color='k', show=False):
  """
  Draws points on the x axis with colors based on their classes.

  Parameters:
    - x: x-coordinate of the circle's center
    - y: y-coordinate of the circle's center
    - r: radius of the circle
    - c: color of the circle
  """
  p = p or configure_graph()

  if isinstance(x, Iterable) and isinstance(y, Iterable) and isinstance(r, Iterable):
    if len(x) == len(y) and len(x) == len(y):
      if isinstance(c, Iterable) and len(x) == len(c):
        for i in range(len(x)): p = draw_circle(p, x[i], y[i], r[i], c[i], alpha, edge_color, show=False)
      else:
        for i in range(len(x)): p = draw_circle(p, x[i], y[i], r[i], None, alpha, edge_color, show=False)
    else: raise ValueError("x size does not match y size")
  else:
    p.gca().add_patch(
      p.Circle((x, y), r, facecolor=c, fill=True, alpha=alpha, edgecolor=edge_color)
    )

  if show: s(p)
  return p