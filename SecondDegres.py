import numpy 
from math import *

# On met dans ce fichier la fonction modifiée pour résoudre un polynome de degré 2 
def SecondDegres(a,b,c):
	# Classiquement le polynome est ax²+bx+c 
	
	# On calcule le discriminant 
	Delta = b**2 - 4*a*c
	
	if (Delta >= 0):
		x1 = (-b - sqrt(Delta))/(2*a)
		x2 = (-b + sqrt(Delta))/(2*a)
		
		# On renvoie le couple 
		return [x1, x2]
	else: 
		# On ne prend pas de nombres complexes
		# On renvoie simplement une liste vide 
		
		return []
		
