"""
Minimal Iterative Optimizer by Yvette Dimitrova and Igor Trujnara. MIT license.
"""

from __future__ import annotations
import sympy
from golden_search import G_Search
from search import Midpoint_Search


class Optimizer:
    def __init__(self, indict):
        # unpack the dict object into variables
        self.varname = indict["varname"]
        self.func = indict["func"]
        self.exec = sympy.lambdify(self.varname, sympy.parse_expr(self.func))
        self.lower = indict["lower"]
        self.upper = indict["upper"]
        self.mode = indict["mode"]
        self.target = indict["target"]
        self.limittype = indict["limittype"]
        self.limitval = indict["limitval"]

        # run the correct optimization function and save the results
        if self.mode == "Equal Interval":
            (
                self.optpos,
                self.optval,
                self.generations,
            ) = Midpoint_Search.midpoint_search(
                self.exec, self.lower, self.upper, self.limittype, self.limitval, self.target
            )
        else:
            (self.optpos, self.optval, self.generations) = G_Search.GOLDEN_search(
                self.exec,
                self.lower,
                self.upper,
                self.limittype,
                self.limitval,
                self.target,
            )

    def get(self):
        """
        Returns the optimization result for external use.
        """
        data = {
            "func": self.func,
            "exec": self.exec,
            "varname": self.varname,
            "lower": self.lower,
            "upper": self.upper,
            "mode": self.mode,
            "limittype": self.limittype,
            "limitval": self.limitval,
            "optpos": self.optpos,
            "optval": self.optval,
            "generations": self.generations,
            "target": self.target,
        }
        return data


"""
class optimizer(d):
  def __init__(self):
    self.dictionary()
  def opt(dictionary):
    return(G_search(self.dictionary(midpoint_search(func, lower, upper, niter)))
"""
