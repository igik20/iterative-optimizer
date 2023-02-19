# Minimal Iterative Optimizer
A simple Python program for finding local extrema of single-variable functions using iterative methods. Includes calculation and plotting functionality.

## Installation
1. Download this repository. You can do this using `git clone` or by downloading a ZIP. If you downloaded a compressed directory, extract it anywhere on your disk.
2. Make sure to install dependencies. Refer to the section below for details.
3. Run the main file by using the command `python3 main.py`.

## Dependencies
To run this program properly, you will need Python 3 (tested on version 3.8, but should work on lower ones as well).

Additionally, you will need the following Python packages:
- tkinter
- customtkinter
- PIL
- matplotlib
- numpy
- sympy

If you are a Debian Linux user, you can use the provided installation script `dependencies.sh`. It requires superuser privileges for certain installations.

### Remark on Anaconda
The program suffers from a known issue with Tkinter font rendering in Conda environments. For this reason, it is recommended to run it outside of Conda, using system Python.

## Quickstart
### Input window
Fill out the fields according to their descriptions. Use Python-like format for the function. Press the button on the bottom to submit. If there are any errors, change the values accordingly.
### Output window
Select the iteration you want to plot, or the final result. Press the button to display the plot.

## Algorithms
### Equal Interval Search
This is an iterative optimization algorithm based on an approximation of the derivative. It works by assessing the function on two values close to the midpoint of the search interval and assuming the local trend is globally applicable. Each iteration halves the size of the search interval.
### Golden Search
This algorithm has a similar concept, but instead uses two intermediate points that divide the search interval according to the golden ratio. It is generally expected to converge faster than Equal Interval Search.
### Remarks on applicability
The algorithms used are only computational approximation methods, and will not always produce reasonable results. The program is only guaranteed to provide a correct approximation for 'well-behaved' functions, which means they satisfy at least the following:
- the function is defined for all values in the search interval
- the function is continuous in the entire search interval
- the extremum of the function in the search interval is finite, and is not asymptotically small.

Additionally, for multimodal functions, the algorithms will only converge to one of the extrema of the desired type.

## Detailed input reference
### Function
The function should be a valid expression, written with a syntax accepted by the Sympy expression parser. Refer to [SymPy documentation](https://docs.sympy.org) for details.
### Variable name
It should only contain a single alphabetic character.
### Lower and upper bound
These should be valid floating-point numbers, written according to Python rules (in particular, using a dot as the decimal separator).
### Optimization algorithm
Choose from a list &ndash; see details above.
### Optimization target
Choose from list &ndash; minimum or maximum.
### Limit type and value
Limit value should be a valid positive floating-point number for absolute or relative tolerance, and a valid positive integer for number of iterations. See details of all modes below.

## Limit conditions
### Number of iterations
The algorithm will only run for the number of iterations indicated by the user.
### Absolute tolerance
The algorithm will only run until the size of the search interval falls below the value indicated.
### Relative tolerance
The algorithm will only run until the ratio of the interval size to magnitude falls below the value indicated. The formula for the ratio is `(upper - lower) / mid` for Equal Interval and `(upper - lower) / lower` for Golden Search.

## Plotting
### Generations
The plot will contain the function in the generation's bounds. The point(s) used for optimization will be indicated.
### Final result 
The plot will contain the function in the original bounds, the location on the extremum, and the value of the function.

## Final remarks
This program was developed for the Algorithms & Data Structures course by Jos&eacute; Lu&iacute;s Balc&aacute;zar et al.

In case of issues, doubts or suggestions, contact us through this repository or by email to [igor.trujnara@alum.esci.upf.edu](mailto:igor.trujnara@alum.esci.upf.edu).