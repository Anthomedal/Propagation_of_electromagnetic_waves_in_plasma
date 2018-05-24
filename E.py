from math import *
import numpy 
from Omega import *
from nglobal import n

# On définit ici les fonction permettant de calculer les composantes Ex et Ey du champ électrique 
def Ex(E, Eprec, vy):
	# Cette fonction va renvoyer la répartition de Ex au temps t+dt
	# E : Ex à t
	# Eprec : Ex à t-dt 
	# vy : vy à t 
	
	# On place n en variable gloable 
	global n 

	# Déclaration du vecteur qu'on veut renvoyer  
	e = numpy.zeros([1,n])
	
	# Construction du vecteur 
	for i in numpy.arange(0, n, 1):
		# On définit des variables intermédiaires pour éviter les calculs redondants 
		w2 = OmegaPe(i)**2
		den = 1 + w2/12
		
		e[0,i] = ((2 - (5/6)*w2)/(den))*E[i] - Eprec[i] - (w2*vy[i])/den
		
	return e 

def Ey(E, Eprec, vx):
	# Cette fonction va renvoyer la répartition de Ey au temps t+dt 
	# E : Ey à t
	# Eprec : Ey à t-dt 
	# vx : vx à t 
	
	# On place n en variable globale 
	global n 

	# Déclaration du vecteur qu'on veut renvoyer 
	e = numpy.zeros([1,n])
	
	# Construction du vecteur 
	for i in numpy.arange(1, n-1, 1):
		# Inutile d'effectuer plusieurs fois le calcul
		w2 = OmegaPe(i)**2
		
		coeff = 1/(1+w2/2)
		
		e[0,i] = coeff*(E[i+1] + E[i-1] + w2*vx[i]) - Eprec[i]
		
	return e 
	
# On ajoute encore une fonction pour calculer les deux composantes en même temps 
def E(E, Eprec, v):
	# cE : composé de Ex et Ey 
	# Eprec : composé de Ex(t-dt) et Ey(t+dt)
	# v : composé de vx(t) et vy(t)
	
	# On place n en variable globale 
	global n 

	# On déclare ce qu'on veut renvoyer 
	Er = numpy.zeros([2,n])
	
	# On construit le champ avec les fonctions précédentes 
	Er[0,] = Ex(E[0,], Eprec[0,], v[1,])
	Er[1,] = Ey(E[1,], Eprec[1,], v[0,])
	
	return Er
