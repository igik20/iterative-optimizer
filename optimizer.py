from __future__ import annotations
from typing import Tuple, Callable, Any, Literal

def optimizer_alg(function: Callable[[Real, Any], Real],
                          bounds: Tuple[Real, Real],
                          epsilon: Real = 1e-5,
                          type_optimization: Literal['min', 'max'] = 'min',
                          max_iter: int = 500,
                          verbose: bool = False,
                          keep_history: bool = False,
                          **kwargs) -> Tuple[Point, HistoryGSS]:



'''
class optimizer(d):
  def __init__(self):
    self.dictionary()
  def opt(dictionary):
    return(G_search(self.dictionary(midpoint_search(func, lower, upper, niter)))
'''
