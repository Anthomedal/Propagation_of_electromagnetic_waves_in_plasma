from math import *
import numpy 
from Omega import *
from nglobal import n

# On définit ici les fonction permettant de calculer les composantes vx et vy de la vitesse 
# On définit les fonctions f et g du schéma 
def f(w, E, v):
	# w : Omega_ce 
	# E : E_x 
	# v : v_y 
	
	a = -w*(E+v)
	
	return a 
	
def g(w, E, v):
	# w : Omega_ce 
	# E: E_y
	# v : v_x 
	
	a = -w*(E-v)
	
	return a 
	
def v(vt, E, Esuiv):
	# vt : vitesse v au temps t 
	# E : Champ E au temps t 
	# Esuiv : Champ E au temps t+dt 
	# Cette fonction renvoie la vitesse au temps t+dt 
	
	# On déclare n comme une variable globale 
	global n 

	# On déclare le vecteur à renvoyer 
	vr = numpy.zeros([2,n])
	
	# Construction du vecteur vr 
	for i in numpy.arange(0, n, 1):
		# On stocke omegace(i) pour les calculs 
		wcei = OmegaCe(i)
		
		# On construit le point E(t+h/2)
		Exint = (E[0,i] + Esuiv[0,i])/2
		Eyint = (E[1,i] + Esuiv[1,i])/2
		
		# Calculs des coeficients de la méthode de Runge-Kutta
		k1 = f(wcei, E[0,i], vt[1,i])
		l1 = g(wcei, E[1,i], vt[0,i])
		
		k2 = f(wcei, Exint, vt[1,i] + l1/2)
		l2 = g(wcei, Eyint, vt[0,i] + k1/2)
		
		k3 = f(wcei, Exint, vt[1,i] + l2/2)
		l3 = g(wcei, Eyint, vt[0,i] + k2/2)
		
		k4 = f(wcei, Esuiv[0,i], vt[1,i] + l3)
		l4 = g(wcei, Esuiv[1,i], vt[0,i] + k3)
		
		vr[0,i] = vt[0,i] + (k1 + 2*k2 + 2*k3 + k4)/6
		vr[1,i] = vt[1,i] + (l1 + 2*l2 + 2*l3 + l4)/6
		
	# Le vecteur vr est construit, on peut le renvoyer 
	return vr 
	

		
