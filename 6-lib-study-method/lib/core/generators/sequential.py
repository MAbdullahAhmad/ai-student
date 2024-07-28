import re
from typing import Callable, List, Dict, Any, Tuple


def parse_function_call(call_str: str) -> Tuple[Callable, List[Any], Dict[str, Any]]:
  """
  Parse a function call string into a function, positional args, and keyword args.
  """
  func_pattern = re.compile(r'(\w+)\s*\((.*)\)')
  match = func_pattern.match(call_str)
  if not match:
    raise ValueError(f"Invalid function call format: {call_str}")
  
  func_name = match.group(1)
  args_str = match.group(2)
  
  # Extract arguments and keyword arguments
  args, kwargs = [], {}
  for arg in args_str.split(','):
    if '=' in arg:
      k, v = arg.split('=', 1)
      kwargs[k.strip()] = eval(v.strip())
    else:
      args.append(eval(arg.strip()))
  
  return func_name, args, kwargs


def sequential(data: Any, function_calls: List[str], functions: Dict[str, Callable]) -> Any:
  """
  Apply a list of function calls sequentially to the data.
  
  :param data: Initial data to be processed.
  :param function_calls: List of function call strings.
  :param functions: Dictionary mapping function names to actual functions.
  :return: Result after applying all function calls.

  ```
  # Example functions
  def add(data, x):
    return data + x

  def multiply(data, y):
    return data * y

  def subtract(data, z):
    return data - z

  # Example usage
  functions = {
    'add': add,
    'multiply': multiply,
    'subtract': subtract
  }

  function_calls = [
    'add($, 3)',
    'multiply($, 2)',
    'subtract($, 1)'
  ]

  result = sequential(5, function_calls, functions)
  print(result)  # Output will be: (5 + 3) * 2 - 1 = 13
  ```
  """
  if not function_calls:
    return data
  
  call_str = function_calls[0]
  func_name, args, kwargs = parse_function_call(call_str)
  
  if func_name not in functions:
    raise ValueError(f"Function '{func_name}' not found in the provided functions dictionary.")
  
  func = functions[func_name]
  
  # Call the function with the current data and other arguments
  data = func(data, *args, **kwargs)
  
  # Recurse with the remaining function calls
  return sequential(data, function_calls[1:], functions)

def generator(functions) -> Callable:
  def func(data, function_calls):
    return sequential(data, function_calls, functions)
  return func