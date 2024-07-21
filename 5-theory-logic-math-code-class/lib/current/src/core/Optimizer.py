from abc import ABC, abstractmethod

class Optimizer(ABC):
  """
  Optimizer class

  Required Methods:
  - update

  Required Props:
  - MODES
  - mode
  """

  MODES = {
    'SAMPLE': 1,
    'BATCH': 2,
  }
  mode = MODES['BATCH']


  @abstractmethod
  def update(self, *args, **kwargs): pass
