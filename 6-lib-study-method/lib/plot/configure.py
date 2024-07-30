import matplotlib.pyplot as plt


graph_settings = {
  "styles": None,
  "size": False,
  "grid": True,
  "center_zero": True,
  "equal_axis": True,
}


def configure_raw(custom_settings):
  global graph_settings
  graph_settings.update(custom_settings)


def get_graph(p=None):
  global graph_settings
  p = p or plt

  # Apply the settings to the p object
  if graph_settings["styles"]:     p.style.use(graph_settings["styles"])
  if graph_settings["size"]:       p.figure(figsize=graph_settings["size"])
  if graph_settings["grid"]:       p.grid(True)
  if graph_settings["equal_axis"]: p.axis('equal')

  if graph_settings["center_zero"]:
    p.axhline(0, color='black',linewidth=0.5)
    p.axvline(0, color='black',linewidth=0.5)

  return p



def configure_graph(p=None, styles=None, size=(10, 10), grid=True, center_zero=True, equal_axis=True):
  global graph_settings

  if styles      is not None:  graph_settings["styles"     ] = styles
  if size        is not None:  graph_settings["size"       ] = size
  if grid        is not None:  graph_settings["grid"       ] = grid
  if center_zero is not None:  graph_settings["center_zero"] = center_zero
  if equal_axis  is not None:  graph_settings["equal_axis" ] = equal_axis
  
  return get_graph(p)
