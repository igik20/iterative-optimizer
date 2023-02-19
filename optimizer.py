from __future__ import annotations
from typing import Tuple, Callable, Any, Literal
from golden_search.py import*
from search.py import*

Class Optimizer:
  def __init__(self):
    #not sure in the keys should be in quotation marks or not :(
  dict = {"function": Callable[[Real, Any], Real],
          "varname": Any,
          "lower": Real,
          "upper": Real,
          "mode": Literal["Equal Interval", "Golden Search"] = "Golden Search",
          "limittype": Literal["Absolute Tolerance:", "Relative Tolerance:", "Number of Iterations:"] = "Absolute Tolerance",
          "limitval": Real}
  mode = mode.lower().strip()
  assert mode in ["Equal Interval", "Golden Search"], 'Invalid mode. Enter "Equal Interval" or "Golden Search"'
  if mode == "Equal Interval" or mode == "equal interval":
    return Modpoint_Search.midpoint_search(func, lower, upper, limitval) #not sure about the limitval here
  else:
    return G_Search.GOLDEN_search(func, lower, upper, limitval)
    
    


'''
class optimizer(d):
  def __init__(self):
    self.dictionary()
  def opt(dictionary):
    return(G_search(self.dictionary(midpoint_search(func, lower, upper, niter)))
'''
