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
		
def SupSecondDegres(a,b, c, alpha, beta):
	# Dans cette fonction on se donne ax²+bx+c définie sur [alpha,beta] et on cherche en quel point le sup |f| est atteint 
	# Elle renvoie une liste [x,P(x)] où x est le point où le sup est atteint 
	
	# On déclare une variable intermédiaire 
	gamma = -(b/2*a)
	
	# On distingue les cas 
	if (gamma > alpha and gamma < beta):
		# Cas gamma € ]alpha,beta[
		if (a < 0):
			# Le maximum est forcément atteint en gamma 
			
			P = a*(gamma**2) + b*gamma + c 
			
			# On renvoie la valeur max et gamma
			return [P, gamma]
			
		if (a > 0):
			# Ce cas est plus complexe 
			P_alpha = abs(a*(alpha**2) + b*alpha + c)
			P_beta = abs(a*(beta**2) + b*beta + c)
			P_gamma = abs(a*(gamma**2) + b*gamma + c)
			
			if (P_alpha > P_beta and P_alpha > P_gamma):
				# P_alpha est le plus grand 
				return [P_alpha, alpha]
				
			if (P_beta > P_alpha and P_beta > P_gamma):
				# P_beta est le plus grand 
				return [P_beta, beta]
			
			if (P_gamma > P_beta and P_gamma > P_alpha):
				# P_gamma est le plus grand 
				return [P_gamma, gamma]
				
				
	else:
		# Cas gamma non € ]alpha,beta[
		# On a juste le choix entre alpha et beta 
		P_alpha = abs(a*(alpha**2) + b*alpha + c)
		P_beta = abs(a*(beta**2) + b*beta + c)
		
		if (P_alpha > P_beta):
			return [P_alpha, alpha]
			
		else:
			return [P_beta, beta]
