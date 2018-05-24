import numpy 
from Trouvermax import *
from matplotlib import pyplot as plt

# On place dans ce fichier la fonction qui calcule la vitesse de groupe du signal 
def milieu(enveloppe):
	# enveloppe : matrice a deux lignes qui contient en sa premiere ligne les valeurs de l'enveloppe et en sa seconde, les abcisses 
	# Cette fonction va renvoyer le meilleur point milieu de l'enveloppe (entre les points d'inflexion) pour calculer Vg
	
	# On sauvegarde la taille 
	n = numpy.size(enveloppe[0,:])

	# On déclare le vecteur des dérivées 
	derivee = numpy.zeros([2,n-2])
	
	# On forme le tableau des dérivées
	for i in numpy.arange(0, n-2, 1):
		# On calcule la valeur de la dérivée
		derivee[0,i] = (enveloppe[0,i-1] - enveloppe[0,i+1])/(enveloppe[1,i-1] - enveloppe[1,i+1])
		
		# On sauvegarde l'abcisse associé
		derivee[1,i] = enveloppe[1,i]
		
	# On transforme toutes les dérivées en leur valeur absolue
	derivee[0,] = numpy.abs(derivee[0,])
	
	# On remplit une matrice formée des points d'inflexions et leurs abcisses
	inflex = TrouverMax(derivee)
	
	# A ce stade inflex contient en sa premiere ligne les valeurs maximales des derivees 
	# Et en sa seconde ligne les abcisses correspondant 
	
	# On vérifie si il y a bien 2 points d'inflexion
	if (numpy.size(inflex[0,]) > 2):
		# On prévient l'utilisateur
		print("Trop de points d inflexion : calcul de la vitesse de groupe impossible")
		print("Tentative de selection des points d inflexion")
		print("...")

		# On fait une boucle sur la taille de inflex 
		while (numpy.size(inflex[0,:])>2):
			# On cherche le minimum des valeurs des points d'inflexion 
			Taille = numpy.size(inflex[0,:]) 

			min = inflex[0,0]

			for i in numpy.arange(0, Taille, 1):
				if (inflex[0,i] <= min):
					# On sauvegarde la valeur minimale
					min = inflex[0,i]

					# On sauvegarde l'indice correspondant 
					indice = i 

			# A la sortie de cette boucle, on dispose de l'indice de la plus petite valeur de inflex
			# Supprimons la
			inflex = numpy.delete(inflex, indice, axis=1)

		print("Epuration des points d inflexion terminee")

		# On relève le point milieu 
		mi = inflex[1,0] + inflex[1,1]
		mi = mi/2 
		
		return mi 

	elif (numpy.size(inflex[0,]) < 2):
		print("Erreur fatale, pas assez de points d inflexion")

	else:
		# On se place dans le cas où il y a bien deux points 
		# On relève le point milieu 
		mi = inflex[1,0] + inflex[1,1]
		mi = mi/2 
		
		return mi 
	
def Vg(enveloppeprec, enveloppe):
	# enveloppeprec : matrice a deux lignes qui contient en sa premiere ligne les valeurs de l'enveloppe et en sa seconde, les abcisses au temps t-1
	# enveloppe : matrice a deux lignes qui contient en sa premiere ligne les valeurs de l'enveloppe et en sa seconde, les abcisses au temps t
	# On calcule ici la vitesse de groupe 
	
	# On sauvegarde les deux abcisses dont on veut calculer la vitesse
	xprec = milieu(enveloppeprec)
	x = milieu(enveloppe)

	# On calcule la vitesse de groupe
	vg = x - xprec
	
	return vg
	

