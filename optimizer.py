from __future__ import annotations
import sympy
from golden_search import G_Search
from search import Midpoint_Search


class Optimizer:
    def __init__(self, indict):
        # unpack the dict object into variables
        self.func = sympy.labmdify(sympy.parse_expr(indict["function"]))
        self.varname = indict["varname"]
        self.lower = indict["lower"]
        self.upper = indict["upper"]
        self.mode = indict["mode"]
        self.limittype = indict["limittype"]
        self.limitval = indict["limitval"]

        # run the correct optimization function and save the results
        if self.mode == "Equal Interval":
            (
                self.maxcoord,
                self.maxval,
                self.generations,
            ) = Midpoint_Search.midpoint_search(
                self.func, self.lower, self.upper, self.limittype, self.limitval
            )
        else:
            (
                self.maxcoord, 
                self.maxval, 
                self.versiq = G_Search.GOLDEN_search(
                self.func, self.lower, self.upper, self.limittype, self.limitval, self.versiq
            )
                #self.func is not directly used in GOLDEN_search, but we use 2 values directly, not a function

    def get(self):
        data = {
            "function": self.func,
            "varname": self.varname,
            "lower": self.lower,
            "upper": self.upper,
            "mode": self.mode,
            "limittype": self.limittype,
            "limitval": self.limitval,
            "maxcoord": self.maxcoord,
            "maxval": self.maxval,
            "generations": self.generations
            "version": self.version
        }
        return data


"""
class optimizer(d):
  def __init__(self):
    self.dictionary()
  def opt(dictionary):
    return(G_search(self.dictionary(midpoint_search(func, lower, upper, niter)))
"""
