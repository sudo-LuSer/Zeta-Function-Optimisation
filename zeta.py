import cmath 
import math  
import numpy as np
from scipy.integrate import quad 
from matplotlib.pylab import plt
epsilon = 10**-1
def F(x,s):
	return (x**(s-1))/(numpy.exp(x)-1)
def zeta(s):
	integration = quad(lambda x: (x**(s-1))/(np.exp(x)-1),0,np.inf)[0]
	InverseGamma = 1/math.gamma(s)
	return InverseGamma*integration
def zetaNegativeValues(s):
	return (2**s)*(np.pi**(s-1))*np.sin(np.pi*s/2)*zeta(1-s)
try:
	print(zeta(float(input())))
except RuntimeWarning:
	print(numpy.inf)
except ValueError:
	print(zetaNegativeValues(float(input())))