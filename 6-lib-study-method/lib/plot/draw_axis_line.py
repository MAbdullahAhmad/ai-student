from .show import show as s
from .configure import configure_graph

def draw_axis_line(p=None, position=0, axis='x', color=None, style=None, label=None, show=False):
  """
  draw a perpendicaulr line on given axis

  Parameters:
  axis (str): Specifies whether to draw the line perpendicular to the 'x' or 'y' axis.
  position (float): The position at which to draw the perpendicular line.
  """

  p = p or configure_graph()

  if axis not in ['x', 'y']:
    raise ValueError("Invalid value for 'axis'. Use 'x' or 'y'.")

  if axis == 'x':   p.axvline(x=position, color=color or 'black', linestyle=style, label=label)
  elif axis == 'y': p.axhline(y=position, color=color or 'black', linestyle=style, label=label)


  if show: s(p)

  return p