import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from .show import show as s
from .configure import configure_graph

def draw_plane(p=None, coef=(1, 2), intercept=0, range=((-1, 10), (-1, 10)), show=False, color='cyan', alpha=0.7, rstride=100, cstride=100, edgecolor='none', elev=30, azim=30):
  """
  Draw a plane on a 3D graph

  Example usage:
  ```py
  coef_x = 0.9
  coef_y = 1.2
  intercept = 1.3

  draw_plane(plt, (coef_x, coef_y), intercept, show=True)
  ```
  """

  coef_x, coef_y = coef
  range_x, range_y = range

  p = p or configure_graph()

  # Check if there are existing axes with a 3D projection
  existing_ax = None
  for ax in p.get_fignums():
    fig = p.figure(ax)
    if any(isinstance(a, Axes3D) for a in fig.get_axes()):
      existing_ax = [a for a in fig.get_axes() if isinstance(a, Axes3D)][0]
      break

  if existing_ax is not None:
    ax = existing_ax
  else:
    ax = p.axes(projection='3d')


  x = np.linspace(range_x[0], range_x[1], 100)
  y = np.linspace(range_y[0], range_y[1], 100)
  X, Y = np.meshgrid(x, y)
  Z = coef_x * X + coef_y * Y + intercept

  # ax = p.axes(projection='3d')
  ax.plot_surface(X, Y, Z, color=color, alpha=alpha, rstride=rstride, cstride=cstride, edgecolor=edgecolor)

  ax.view_init(elev=elev, azim=azim)
  
  if show: s(p)

  return p