import numpy 
from Trouvermax import *
from matplotlib import pyplot as plt
from splines import *

# On place dans ce fichier la fonction qui calcule la vitesse de groupe du signal 
def Vg(signalprec, signalsuiv, v_g):
	# signalprec : matrice a deux lignes qui contient en sa premiere ligne les valeurs des maximums du signal et en sa seconde, les abcisses au temps t-1
	# signalsuiv : matrice a deux lignes qui contient en sa premiere ligne les valeurs des maximums du signal et en sa seconde, les abcisses au temps t
	# On calcule ici la vitesse de groupe 
	
	# On sauvegarde les deux abcisses dont on veut calculer la vitesse
	xprec = splines(signalprec, [], 1)
	xsuiv = splines(signalsuiv, [], 1)

	# On calcule la vitesse de groupe
	vg = (v_g + (xsuiv - xprec)/2)/2
	
	return vg
	

