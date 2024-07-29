from mpl_toolkits.mplot3d import Axes3D

from .show import show as s
from .configure import configure_graph

def draw_3d_scatter(p=None, x=[], y=[], z=[], show=False, elev=30, azim=30):
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

  # ax = p.axes(projection='3d')

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

  ax.scatter(x, y, z)
  ax.view_init(elev=elev, azim=azim)

  if show: s(p)

  return p