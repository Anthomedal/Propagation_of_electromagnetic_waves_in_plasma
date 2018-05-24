from math import *
import numpy 
from nglobal import n

# On définit ici la fonction qui produit le vecteur formé de la répartition initiale de la vitesse
def VInit():
	# On met n en globale  
	global n 

	# Déclaration de E 
	v = numpy.zeros([2,n]) 
	
	# On construit le vecteur 
	for i in numpy.arange(0, n, 1):
		# On remplace dans la formule suivante la fonction qu'on veut pour les valeurs initiales de E
		v[0,i] = 0
		v[1,i] = 0
		
	return v
