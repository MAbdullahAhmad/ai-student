# from .show import show as s

# from .configure import configure_graph

# def draw_scatter(p=None, x=[], y=None, show=False):
#   """
#   draw scatter plot

#   ```py
#   # Example usage:
#   x = [1, 2, 3, 4, 5]
#   y = [2, 3, 5, 4, 6]

#   draw_scatter(plt, x, y, show=True)
#   ```
#   """

#   p = p or configure_graph()
#   y = y or list(range(len(x)))

#   p.scatter(x, y)
#   if show: s(p)

#   return p


import numpy as np
from .show import show as s
from .configure import configure_graph

def draw_scatter(p=None, x=[], y=None, classes=None, colors=None, show=False):
  """
  Draw scatter plot with colors based on classes.

  Parameters:
  p: pyplot obj (optional)
  x (list or array): List or array of x coordinates.
  y (list or array): List or array of y coordinates.
  classes (list or array, optional): List or array of class labels corresponding to each point. If None, all points are colored the same.
  colors (list or array, optional): List or array of colors corresponding to each class. If None, a colormap is used.
  show (bool): Optional, whether to show the plot.

  Example usage:
  x = [1, 2, 3, 4, 5]
  y = [2, 3, 5, 4, 6]
  classes = [0, 1, 0, 1, 0]
  colors = ['red', 'blue']
  draw_scatter(plt, x, y, classes=classes, colors=colors, show=True)
  """

  p = p or configure_graph()
  y = y or list(range(len(x)))

  if classes is None:
    p.scatter(x, y)
  else:
    # Unique classes
    unique_classes = sorted(set(classes))

    # Use a default colormap if no colors are provided
    if colors is None:
      colors = p.get_cmap('tab10', len(unique_classes))
      colors = [colors(i) for i in range(len(unique_classes))]
    else:
      if len(colors) < len(unique_classes):
        raise ValueError("Not enough colors provided for the number of unique classes.")
      colors = colors[:len(unique_classes)]

    # Map classes to colors
    color_map = {cls: colors[i] for i, cls in enumerate(unique_classes)}

    # Scatter plot with colors based on classes
    for cls in unique_classes:
      cls_indices = [i for i, c in enumerate(classes) if c == cls]
      p.scatter(np.array(x)[cls_indices], np.array(y)[cls_indices], color=color_map[cls], label=f'Class {cls}')

  if show: s(p)

  return p
