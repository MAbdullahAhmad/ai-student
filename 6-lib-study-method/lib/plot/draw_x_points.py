from .draw_axis_points import draw_axis_points

def draw_x_points(p=None, points=[], classes=[], colors=None, labels=None, show=False):
  """
  Draws points on the x axis with colors based on their classes.

  Parameters:
  p: pyplot obj (optional)
  points (list or array): List or array of (x, y) coordinates of the points.
  classes (list or array): List or array of class labels corresponding to each point.
  colors (list or array, optional): List or array of colors corresponding to each class. If None, a colormap is used.
  show (bool): optional
  """

  return draw_axis_points(p, points, classes, 'x', colors, labels, show)