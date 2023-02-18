'''
GOLDEN SEARCH ALGORITHM
'''
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
#Here we are importing all the required libraries needed for the construction and implementation of the Golden Search Algorithm.

class G_Search(d):
	def __init__(self):
		self.d ={}
	#This chunck of code checks whether a is bigger than b and prints a variable, which we called 'status'. This is really important
	#for the overall algorithm because we want to check the location of the points in terms of each other.
	def imput_check(a, b):
		if b<a:
			status='correct'
		else:
			status='wrong'
		return status

	#Central for the Golden Search Algorithm is checking which is the extremum value inside the sin graph. For this purpose, we are
	#using the np library to create a function which returns the sin of a value.
	def sin_grab(x):
		our_sin=np.sin(x)
		return our_sin

	#Here we are making sure that the interior values do not surpass the boundry values.
	#bup: upper boundry value
	#blow: lower boundry value
	
	def boundry_insidepts(blow, bup):
		z =((np.sqrt(5)-1)/2)*(bup-blow)
		a = blow + z
		b = bup - z
		return a, b
	
	#Now we want to want to optimize the function by selecting an optimal point. Here we will have 2 functions which represent
	#2 different cases - a minimal golden search and a maximum golden search. The criteria for selecting that optimal point will 
	#differ for both cases mentioned above, therefore we will have the 2 following functions - min_search and max_search.
	#opt_pt: optimal point 
	#new_pt: new point, using the function boundry_insidepts
	
	def min_search(blow, bup, a, b, status):
		f1 = sin_grab(a)
		f2 = sin_grab(b)
		if status=='correct' and f2>f1:
			blow = b
			bup = bup
			new_pt = boundry_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = a
		else:
			blow = blow
			bup = a
			new_pt = boundry_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = b
		return blow, bup, opt_pt

	def max_search(blow, bup, a, b, status):
		f1 = sin_grab(a)
		f2 = sin_grab(b)
		if status=='correct' and f2>f1:
			blow = blow
			bup = a
			new_pt = boundry_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = b
		else:
			blow = b
			bup = bup
			new_pt = boundry_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = a
		return blow, bup, opt_pt

#Lastly, we will create the final function called Golden Search which is using all the functions above to represent the Golden
#Search Algorithm.
#

	def GOLDEN_search(blow, bup, versiq, error_trash):
		iteration = 0
		our_e = 1
		while error_trash<=our_e:
			new_pt = boundry_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			f1 = sin_grab(a)
			f2 = sin_grab(b)
			status = imput_check(a, b)
			clear_output(wait=True)
			
			
			plot_graph(blow, bup, a, b)
			plt.show()
			
			
			if versiq=='max':
				bnew = max_search(blow, bup, a, b, status)
			elif versiq=='min':
				bnew = min_search(blow, bup, a, b, status)
			else:
				print('Min/Max status not definded properly.')
				break
			blow = bnew[0]
			bup = bnew[1]
			opt_pt = bnew[2]
			
			iteration+=1
			print ('Iteration: ', iteration)
			ratio=(np.sqrt(5)-1)/2
			our_e=((1-r)*(abs((xu-xl)/xopt)))*100
			print('Error:', our_e)
			time.sleep(1)
