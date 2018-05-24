import numpy 

# Cette fonction permet de trouver les maximums d'une série de données
def TrouverMax(x):
	# On cherche les differents pics de x 
	# x est une matrice comprenant en première ligne les valeurs et en deuxième ligne les abcisses
	n = numpy.size(x[0,])
	
	# n est la longueur de x 
	
	# On construit la matrice qui va comporter les abscisses et les ordonnées des maximums 
	coord = numpy.zeros([2,n])
	
	# Une variable k pour remplir coord 
	k = int(0)
	
	# On parcourt x 
	for i in numpy.arange(1, n-1, 1):
		if (x[0,i]>x[0,i-1] and x[0,i]>x[0,i+1]):
			# On est dans le cas où x[i] est un maximum 
			
			# On sauvegarde la valeur
			coord[0,k] = x[0,i] 
			
			# On sauvegarde l'abscisse
			coord[1,k] = x[1,i]
			#print(coord[1,k])
			
			# On passe à la colonne suivante de coord
			k = k+1
			
	# A la sortie de la boucle k est le nombre de maximums 
	# On renvoie ce qui nous intéresse 
	
	return coord[0:2,0:k]


	
	
	
