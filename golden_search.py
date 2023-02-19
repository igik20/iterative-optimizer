'''
GOLDEN SEARCH ALGORITHM
'''
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
#Here we are importing all the required libraries needed for the construction and implementation of the Golden Search Algorithm.

class G_Search:
	
	def sin_grab(x):
		our_sin=np.sin(x)
		return our_sin

	#Here we are making sure that the interior values do not surpass the boundary values.
	#bup: upper boundary value
	#blow: lower boundary value
	
	def boundry_insidepts(blow, bup):
		z =((np.sqrt(5)-1)/2)*(bup-blow)
		a = blow + z
		b = bup - z
		return a, b
	
	#Now we want to want to optimize the function by selecting an optimal point. Here we will have 2 functions which represent
	#2 different cases - a minimal golden search and a maximum golden search. The criteria for selecting that optimal point will 
	#differ for both cases mentioned above, therefore we will have the 2 following functions - min_search and max_search.
	#opt_pt: optimal point 
	#new_pt: new point, using the function boundary_insidepts
	
	def min_search(blow, bup, a, b):
		f1 = sin_grab(a)
		f2 = sin_grab(b)
		if f2>f1:
			blow = b
			bup = bup
			new_pt = self.boundary_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = a
		else:
			blow = blow
			bup = a
			new_pt = self.boundary_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = b
		return blow, bup, opt_pt

	def max_search(blow, bup, a, b):
		f1 = sin_grab(a)
		f2 = sin_grab(b)
		if f2>f1:
			blow = blow
			bup = a
			new_pt = self.boundary_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = b
		else:
			blow = b
			bup = bup
			new_pt = self.boundary_insidepts(blow, bup)
			a = new_pt[0]
			b = new_pt[1]
			opt_pt = a
		return blow, bup, opt_pt

#Lastly, we will create the final function called Golden Search which is using all the functions above to represent the Golden
#Search Algorithm.
#

#limittype and limval are not defined and have not been defined in any of the functions above
	def GOLDEN_search(blow, bup, limittype, limval, version):
		ABSMAX = 10**6
		iteration = 0
		new_pt = self.boundary_insidepts(blow, bup)
		a = new_pt[0]
		b = new_pt[1]
		f1 = sin_grab(a)
		f2 = sin_grab(b)	
			
		put_check(a, b)
		clear_output(wait=True)
			
			
		plot_graph(blow, bup, a, b)
		plt.show()
		
		while True:
			if limtype == "Number of Iterations" and iteration >= limval:
				break
			elif limtype == "Absolute Tolerance" and bup - blow <= limval:
				break
			elif limtype == "Relative Tolerance" and (bup - blow) / blow <= limval:
				break
			elif iteration >= ABSMAX:
				break

			if version=='max':
				bnew = max_search(blow, bup, a, b, status)
			elif version=='min':
				bnew = min_search(blow, bup, a, b, status)
			else:
				print('Min/Max status not definded properly.')
				break
		
		return bnew
		blow = bnew[0]
		bup = bnew[1]
		opt_pt = bnew[2]
		iteration+=1
		#print ('Iteration: ', iteration)
		time.sleep(1)
			
			
	def plot_graph(blow,bup,a,b):
		clear_output(wait=True)
		
		#basic plotting, sin graph and coordinate sys
		plt.plot(x,y)
		plt.plot([0,6],[0,0],'k')
		
		#plotting blow line
		plt.plot([blow,blow],[0,sin_grab(blow)])
		plt.annotate('lower limit',xy=(blow-0.01,-0.2))
		
		#plotting bup line
		plt.plot([bup,bup],[0,sin_grab(bup)])
		plt.annotate('upper limit',xy=(bup-0.01,-0.2))

		#plotting the first point
		plt.plot(a,sin_grab(a),'ro',label='a')
		plt.plot([a,a],[0,sin_grab(a)],'k')
		#plotting the second point
		plt.plot(b,sin_grab(b),'bo',label='b')
		plt.plot([b,b],[0,sin_grab(b)],'k')

		#plotting the first line, associated with a
		plt.plot([a,a],[0,sin_grab(a)],'k')
		plt.annotate('a',xy=(a-0.01,-0.2))

		#plotting the second line, associated with b
		plt.plot([b,b],[0,sin_grab(b)],'k')
		plt.annotate('b',xy=(b-0.01,-0.2))

		#setting the limit of the window:
		plt.ylim([-1.3,1.3])
		plt.show()
