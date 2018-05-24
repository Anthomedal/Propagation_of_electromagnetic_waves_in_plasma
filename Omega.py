from math import *
import numpy
from nglobal import n 

# On définit ici les fonctions permettant de calculés les omega, fixés dans le temps
def OmegaPe(x):
	# Remplacer le terme de droite par ce que l'on souhaite étudier 
	if (x<n/2):
		w = 0.2
	else:
		w = 0.0005*x + 0.2 - 0.0005*(n/2)
	
	return w
	
def OmegaCe(x):
	# Remplacer le terme de droite par ce que l'on souhaite étudier
	w = 0.1
	
	return w
	
