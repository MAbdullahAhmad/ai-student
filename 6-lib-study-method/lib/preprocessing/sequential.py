from ..core.generators.sequential import generator
from . import all

functions = {}
for k in [x for x in dir(all) if x[:2] != '__']:
  functions[k] = getattr(all, k)

sequential = generator(functions)