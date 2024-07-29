from collections.abc import Iterable
from numbers import Number

def simple_mean(values: Iterable[Number]) -> Number:
  return sum(values) / len(values)