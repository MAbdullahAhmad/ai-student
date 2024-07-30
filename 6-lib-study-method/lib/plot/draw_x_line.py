from .show import show as s
from .configure import configure_graph

def draw_x_line(p=None, position=0, color=None, style=None, label=None, show=False):
  """
  draw a perpendicaulr line on x axis

  Parameters:
  position (float): The position at which to draw the perpendicular line.
  """

  p = p or configure_graph()
  p.axvline(x=position, color=color or 'black', linestyle=style, label=label)

  if show: s(p)
  return p