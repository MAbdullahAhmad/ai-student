import numpy as np

from .show import show as s
from .configure import configure_graph

def draw_axis_points(p=None, points=[], classes=[], axis='x', colors=None, labels=None, show=False):
  """
  Draws points on the given axis with colors based on their classes.

  Parameters:
  p: pyplot obj (optional)
  points (list or array): List or array of (x, y) coordinates of the points.
  classes (list or array): List or array of class labels corresponding to each point.
  axis ('x' or 'y'): Axis to plot points on
  colors (list or array, optional): List or array of colors corresponding to each class. If None, a colormap is used.
  show (bool): optional
  """

  p = p or configure_graph()

  # Unique classes
  unique_classes = sorted(set(classes))

  # Use a default colormap if no colors are provided
  if colors is None:
    colors = p.get_cmap('tab10', len(unique_classes))
    colors = [colors(i) for i in range(len(unique_classes))]

  # Otherwise use provided colors
  else:
    if len(colors) < len(unique_classes):
      raise ValueError("Not enough colors provided for the number of unique classes.")
    colors = colors[:len(unique_classes)]


  for i, cls in enumerate(unique_classes):
    # Filter points and classes by current class
    cls_points = [point for point, c in zip(points, classes) if c == cls]
    
    lbl = cls if labels else None
    if axis == 'x':   p.scatter(cls_points, np.zeros(len(cls_points)), color=colors[i], label=lbl)
    elif axis == 'y': p.scatter(np.zeros(len(cls_points)), cls_points, color=colors[i], label=lbl)

  # Add legend and labels
  p.legend()
  if labels:
    p.xlabel('X')
    p.ylabel('Y')

  if show: s(p)
  return p