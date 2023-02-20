"""
Minimal Iterative Optimizer by Yvette Dimitrova and Igor Trujnara. MIT license.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# Here we are importing all the required libraries needed for the construction and implementation of the Golden Search Algorithm.


class G_Search:
    def func(x):
        our_sin = np.sin(x)
        return our_sin

    # Here we are making sure that the interior values do not surpass the boundary values.
    # bup: upper boundary value
    # blow: lower boundary value
    @staticmethod
    def boundary_insidepts(blow, bup):
        z = ((np.sqrt(5) - 1) / 2) * (bup - blow)
        a = blow + z
        b = bup - z
        return a, b

    # Now we want to want to optimize the function by selecting an optimal point. Here we will have 2 functions which represent
    # 2 different cases - a minimal golden search and a maximum golden search. The criteria for selecting that optimal point will
    # differ for both cases mentioned above, therefore we will have the 2 following functions - min_search and max_search.
    # opt_pt: optimal point
    # new_pt: new point, using the function boundary_insidepts
    '''
    @staticmethod
    def min_search(func, blow, bup, a, b):
        f1 = func(a)
        f2 = func(b)
        if f2 > f1:
            blow = b
            bup = bup
            new_pt = G_Search.boundary_insidepts(blow, bup)
            a = new_pt[0]
            b = new_pt[1]
            opt_pt = a
        else:
            blow = blow
            bup = a
            new_pt = G_Search.boundary_insidepts(blow, bup)
            a = new_pt[0]
            b = new_pt[1]
            opt_pt = b
        return blow, bup, opt_pt

    @staticmethod
    def max_search(func, blow, bup, a, b):
        f1 = func(a)
        f2 = func(b)
        if f2 > f1:
            blow = blow
            bup = a
            new_pt = G_Search.boundary_insidepts(blow, bup)
            a = new_pt[0]
            b = new_pt[1]
            opt_pt = b
        else:
            blow = b
            bup = bup
            new_pt = G_Search.boundary_insidepts(blow, bup)
            a = new_pt[0]
            b = new_pt[1]
            opt_pt = a
        return blow, bup, opt_pt
'''
    # Lastly, we will create the final function called Golden Search which is using all the functions above to represent the Golden
    # Search Algorithm.
    #

    # limittype and limval are not defined and have not been defined in any of the functions above
    @staticmethod
    def GOLDEN_search(func, blow, bup, limtype, limval, version):
        ABSMAX = 10**6
        iteration = 0
        generations = {}
        new_pt = G_Search.boundary_insidepts(blow, bup)
        a = new_pt[0]
        b = new_pt[1]
        f1 = func(a)
        f2 = func(b)

        #G_Search.plot_graph(blow, bup, a, b)
        #plt.show()

        while True:
            if limtype == "Number of Iterations" and iteration >= limval:
                break
            elif limtype == "Absolute Tolerance" and bup - blow <= limval:
                break
            elif limtype == "Relative Tolerance" and (bup - blow) / blow <= limval:
                break
            elif iteration >= ABSMAX:
                break

            if version == "Maximum":
                f1 = func(a)
                f2 = func(b)
                if f2 > f1:
                    blow = blow
                    bup = a
                    new_pt = G_Search.boundary_insidepts(blow, bup)
                    a = new_pt[0]
                    b = new_pt[1]
                    opt_pt = b
                else:
                    blow = b
                    bup = bup
                    new_pt = G_Search.boundary_insidepts(blow, bup)
                    a = new_pt[0]
                    b = new_pt[1]
                    opt_pt = a
                return blow, bup, opt_pt
                #bnew = G_Search.max_search(func, blow, bup, a, b)
            elif version == "Minimum":
                f1 = func(a)
                f2 = func(b)
                if f2 > f1:
                    blow = b
                    bup = bup
                    new_pt = G_Search.boundary_insidepts(blow, bup)
                    a = new_pt[0]
                    b = new_pt[1]
                    opt_pt = a
                else:
                    blow = blow
                    bup = a
                    new_pt = G_Search.boundary_insidepts(blow, bup)
                    a = new_pt[0]
                    b = new_pt[1]
                    opt_pt = b
                return blow, bup, opt_pt
                #bnew = G_Search.min_search(func, blow, bup, a, b)
            else:
                print("Minimum/Maximum status not definded properly.")
                break
            #history to save information about each iteration
            generations[iteration] = (blow, a, b, bup)
            #next iteration
            iteration+=1
        return bnew, func(bnew), generations

    
    
    @staticmethod
    def plot_generation(func, blow, bup, a, b):
        x = np.linspace(blow, bup, 100)
        y = [func(i) for i in x]
        plt.plot(x, y)
        plt.axvline(x = a, color = "green")
        plt.axvline(x = b, color = "green")
        plt.axvline(x = blow, color = "blue")
        plt.axvline(x = bup, color = "blue")
        plt.show()
        
    @staticmethod
    def plot_result(func, blow, bup, coord, val):
        x = np.linspace(blow, bup, 100)
        y = [func(i) for i in x]
        plt.plot(x, y)
        plt.axvline(x = coord, color = "red")
        plt.axhline(y = val, color = "red")
        plt.show()
    
    
    '''
    @staticmethod
    def plot_graph(func, blow, bup, a, b):
        # basic plotting, sin graph and coordinate sys
        plt.plot(x, y)
        plt.plot([0, 6], [0, 0], "k")

        # plotting blow line
        plt.plot([blow, blow], [0, func(blow)])
        plt.annotate("lower limit", xy=(blow - 0.01, -0.2))

        # plotting bup line
        plt.plot([bup, bup], [0, func(bup)])
        plt.annotate("upper limit", xy=(bup - 0.01, -0.2))

        # plotting the first point
        plt.plot(a, func(a), "ro", label="a")
        plt.plot([a, a], [0, func(a)], "k")
        # plotting the second point
        plt.plot(b, func(b), "bo", label="b")
        plt.plot([b, b], [0, func(b)], "k")

        # plotting the first line, associated with a
        plt.plot([a, a], [0, func(a)], "k")
        plt.annotate("a", xy=(a - 0.01, -0.2))

        # plotting the second line, associated with b
        plt.plot([b, b], [0, func(b)], "k")
        plt.annotate("b", xy=(b - 0.01, -0.2))

        # setting the limit of the window:
        plt.ylim([-1.3, 1.3])
        plt.show()
'''
