from math import *
import numpy 
from nglobal import n

# On définit ici la fonction qui produit le vecteur formé de la répartition initiale du champ élétrique 
def EInit():
	# On met n en globale  
	global n 

	# Déclaration de E 
	E = numpy.zeros([2,n]) 
	
	# On construit le vecteur 
	for i in numpy.arange(0, n, 1):
		# On remplace dans la formule suivante la fonction qu'on veut pour les valeurs initiales de E
		E[0,i] = 0
		#E[1,i] = exp((-(i-250)**2)/3000)*sin(-0.3*i)
		E[1,i] = 0
		
	return E


def Esecond():
	# On met n en globale  
	global n 

	# Déclaration de E 
	E = numpy.zeros([2,n]) 
	
	# On construit le vecteur 
	for i in numpy.arange(0, n, 1):
		# On remplace dans la formule suivante la fonction qu'on veut pour les valeurs initiales de E
		E[0,i] = 0
		#E[1,i] = exp((-(i-250)**2)/3000)*sin(-0.3*i)
		E[1,i] = 0
		
	return E
