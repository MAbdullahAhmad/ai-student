import re
import ast
from typing import Callable, List, Dict, Tuple, Iterable

def parse_function_call(call_str: str) -> Tuple[str, List, Dict]:
  """
  Parse a function call string into a function name, positional args, and keyword args.
  """
  func_pattern = re.compile(r'(\w+)\s*\((.*)\)')
  match = func_pattern.match(call_str)
  if not match:
      raise ValueError(f"Invalid function call format: {call_str}")
  
  func_name = match.group(1)
  args_str = match.group(2)
  
  # Parse the arguments using ast
  try:
      args_list = ast.parse(f'func({args_str})').body[0].value.args
      kwargs_list = ast.parse(f'func({args_str})').body[0].value.keywords
  except SyntaxError as e:
      raise ValueError(f"Syntax error in arguments: {e}")
  
  args = [ast.literal_eval(arg) for arg in args_list]
  kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in kwargs_list}
  
  return func_name, args, kwargs



def sequential(data, function_calls: Iterable[str|Iterable], functions: Dict[str, Callable]):
  """
  Apply a list of function calls sequentially to the data.
  
  :param data: Initial data to be processed.
  :param function_calls: List of function call strings.
  :param functions: Dictionary mapping function names to actual functions.
  :return: Result after applying all function calls.

  ```py
  # Example functions
  def add(data, x):
    return data + x

  def multiply(data, y, z=None):
    return data * y * z if z else data * y

  def subtract(data, value):
    return data - value

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
  print(result)  # Output will be: (5 + 3) * 2 - 1 = 15

  or function_calls can be passed like this:

  function_calls = [
    ['add', 3],
    ['multiply', [2, 2]]',
    ['subtract', {"value": 1}]
  ]

  result = sequential(5, function_calls, functions)
  print(result)  # Output will be: (5 + 3) * 2 * 2 - 1 = 31

  ```
  """

  if not function_calls: return data
  
  func_name = ''
  args = []
  kwargs = {}
  
  current = function_calls[0]

  if isinstance(current, str):
    func_name, args, kwargs = parse_function_call(current)
  
  elif type(current[0]) == str:
    func_name = current[0]

    if len(current) > 1:
      if type(current[1]) == list:
        args = current[1]
      elif type(current[1]) == dict:
        kwargs = current[1]
      else: args = [current[1]]
       
  else: raise ValueError(f"First member of function call must be `str`, {type(current[0])} given.")
  
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