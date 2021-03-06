import numpy 
from SystemesLineaires import *
from matplotlib import pyplot as plt 
from Trouvermax import *
from SecondDegres import *

# On écrit ici les fonctions qui permettent de faire une interpolation par splines cubiques 
def splines(f, x, test):
	# f est une matrice 2 x n qui contient sur sa première ligne les valeurs et sur la seconde les noeuds de l'interpolation
	# x est un vecteur qui contient les points où l'on veut interpoler la fonction 
	# La variable test permet de choisir entre le cas où la fonction est appelée dans le main où dans la recherche de la vitesse de groupe 
	
	if (test == 0):
		# Le cas où la fonction est appelée dans le main 
		n = numpy.size(f[0,])
		# n est le nombre de points à interpoler 
		
		# On refixe n comme dans la méthode 
		n = n-1
		
		# On construit un vecteur qui contient les deltax 
		Delta_x = numpy.zeros([1,n])
		
		for i in numpy.arange(0,n,1):
			Delta_x[0,i] = f[1,i+1] - f[1,i]
			
		# On déclare la matrice du système linéaire associé
		A = numpy.zeros([n+1,n+1])
		
		# On déclare également le vecteur du système 
		b = numpy.zeros([1,n+1])
		
		# On remplit cette matrice et le vecteur
		A[0,0] = 1
		A[n,n] = 1
		b[0,0] = 0
		b[0,n] = 0
		
		for i in numpy.arange(1,n,1):
			A[i,i-1] = Delta_x[0,i-1]
			A[i,i] = 2*(Delta_x[0,i] + Delta_x[0,i-1])
			A[i,i+1] =  Delta_x[0,i]
			
			b[0,i] = 6*(((f[0,i+1]-f[0,i])/Delta_x[0,i]) - ((f[0,i]-f[0,i-1])/Delta_x[0,i-1]))
			
		# Le système linéaire associé à l'interpolation est posé
		# On résoud ce système pour se donner les s 
		s = Tridiagonal(A,b)
		
		# On peut alors construire les coefficients a et b 
		a = numpy.zeros([1,n])
		b = numpy.zeros([1,n])
		
		for i in numpy.arange(0,n,1):
			a[0,i] = f[0,i]/Delta_x[0,i] - (s[0,i]*Delta_x[0,i])/6
			b[0,i] = f[0,i+1]/Delta_x[0,i] - (s[0,i+1]*Delta_x[0,i])/6
			
		# On construit le vecteur à renvoyer 
		k = numpy.zeros([1,numpy.size(x)])
		
		# Cette variable permet de naviguer dans k
		t = 0
		
		for p in x:
			# Cette variable va corriger les décalages 
			test = False
			
			# On parcourt les abscisses
			for i in numpy.arange(0,n,1):
				# On examine la position de p dans l espace 
				if (p>=f[1,i] and f[1,i+1]>=p):
					# On sait que c'est le polynome indicé i qu'il faut utiliser pour interpoler
					k[0,t] = s[0,i]*((f[1,i+1]-p)**3)/(6*Delta_x[0,i]) + s[0,i+1]*((p-f[1,i])**3)/(6*Delta_x[0,i]) + a[0,i]*(f[1,i+1]-p) + b[0,i]*(p-f[1,i])
					
					# On incrémente l'indice du k
					t = t+1
					
					# On indique que le point a bien ete trouvé entre les noeuds
					test = True
					
					# On stop la boucle pour économiser du temps de calcul
					break
					
			# Incrémentation corrective
			if (test == False):
				# Nous sommes dans le cas où le point n'est pas entre les noeuds
				# On met à zero la valeur a renvoyer 
				k[0,t] = 0 
				
				# On incrémente pour ne pas créer de décallage
				t = t + 1
		return k
		
	if (test == 1):
		# Le cas où la fonction est appelée dans Vg
		n = numpy.size(f[0,])
		# n est le nombre de points à interpoler 
		
		# On refixe n comme dans la méthode 
		n = n-1
		
		# On construit un vecteur qui contient les deltax 
		Delta_x = numpy.zeros([1,n])
		
		for i in numpy.arange(0,n,1):
			Delta_x[0,i] = f[1,i+1] - f[1,i]
			
		# On déclare la matrice du système linéaire associé
		A = numpy.zeros([n+1,n+1])
		
		# On déclare également le vecteur du système 
		b = numpy.zeros([1,n+1])
		
		# On remplit cette matrice et le vecteur
		A[0,0] = 1
		A[n,n] = 1
		b[0,0] = 0
		b[0,n] = 0
		
		for i in numpy.arange(1,n,1):
			A[i,i-1] = Delta_x[0,i-1]
			A[i,i] = 2*(Delta_x[0,i] + Delta_x[0,i-1])
			A[i,i+1] =  Delta_x[0,i]
			
			b[0,i] = 6*(((f[0,i+1]-f[0,i])/Delta_x[0,i]) - ((f[0,i]-f[0,i-1])/Delta_x[0,i-1]))
			
		# Le système linéaire associé à l'interpolation est posé
		# On résoud ce système pour se donner les s 
		s = Tridiagonal(A,b)
		
		# On peut alors construire les coefficients a et b 
		a = numpy.zeros([1,n])
		b = numpy.zeros([1,n])
		
		for i in numpy.arange(0,n,1):
			a[0,i] = f[0,i]/Delta_x[0,i] - (s[0,i]*Delta_x[0,i])/6
			b[0,i] = f[0,i+1]/Delta_x[0,i] - (s[0,i+1]*Delta_x[0,i])/6
			
		# On construit le vecteur à renvoyer 
		k = numpy.zeros([1,numpy.size(x)])
		
		# Cette variable permet de naviguer dans k
		t = 0
			
		MaxDerivee = []
		
		# On parcourt les abscisses
		for i in numpy.arange(0,n,1):
			# On enregistre le max de la dérivée du iemm polynome 
			MaxDerivee.append(SupSecondDegres(s[0,i+1] - s[0,i], 2*(f[1,i+1]*s[0,i] - f[1,i]*s[0,i+1]), s[0,i+1]*f[1,i]*f[1,i] - s[0,i]*f[1,i+1]*f[1,i+1], f[1,i], f[1,i+1]))
			 
		# On dispose alors du max des dérivées de chaque polynomes des splines 
		# On trie cette liste 
		
		echange = 1
		
		# On enregistre le nombre d'élément de MaxDerivee
		nb = len(MaxDerivee)
		
		while (echange == 1):
			# La variable echange prend la valeur 1 si un echange a eu lieu, 0 sinon 
			echange = 0
			
			for i in numpy.arange(0, nb-1, 1):
				if (MaxDerivee[i][0] < MaxDerivee[i+1][0]):
					# On inverse les deux valeurs 
					intermediaire = MaxDerivee[i]
					
					MaxDerivee[i] = MaxDerivee[i+1]
					
					MaxDerivee[i+1] = intermediaire
					
					# On signale le fait qu'il y a eu une operation sur la liste
					echange = 1
		
		# A la sortie de ce while on dispose de la liste MaxDerivee triee en valeur decroissante, il suffit de prendre ses deux premiers elements pour travailler
		abcisse = MaxDerivee[0][1] + MaxDerivee[1][1]
		abcisse = abcisse/2
			
		return abcisse
