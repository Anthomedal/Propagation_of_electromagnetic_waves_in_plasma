import numpy 
from math import *

# Dans ce fichier, nous écrivons des fonctions qui permettent de résoudre les systèmes linéaires 
def scalaire(a,b):
	# Cette fonction fait le produit scalaire de a par b 
	n = numpy.size(a)
	
	p = float(0)
	for i in numpy.arange(0,n,1):
		p = p + a[i]*b[i]
		
	return p
	
# Résolution d'un système triangulaire supérieur
def Remonte(A,b):
	# A est une matrice triangulaire supérieure
	# b est le vecteur solution dans Ax=b
	
	# On fixe la taille du système 
	n = numpy.size(b)
	
	# On déclare le vecteur x qu'on souhaite renvoyer 
	x = numpy.zeros([1,n])
	
	# On remonte le système
	for i in numpy.arange(n-1, -1, -1):
		# On crée une variable pour stocker la somme à faire 
		s = 0
		
		# On calcule la somme 
		for j in numpy.arange(i+1, n, 1):
			if (j != n):
				s = s + A[i,j]*x[0,j]
				
		x[0,i] = (b[i] - s)/A[i,i]
		
	# A la sortie de cette boucle le vecteur solution x est construit
	return x 
	
# Résolution d'un système par décomposition QR
def QR(A,b):
	# On résoud le système linéaire par factorisation QR
	
	# On enregistre la taille du système 
	n = numpy.size(b)
	
	# Déclaration de la matrice Householder
	H = numpy.zeros([n,n])
	
	# Initialisation de Q et R 
	Q = numpy.eye(n)
	R = A 
	
	for k in numpy.arange(0, n-1, 1):
		# On stocke la k-ieme colonne de R 
		a = numpy.array(R[k:n,k])
		
		# On construit un vecteur intermédiaire
		d = numpy.array(a)
		d[0] = d[0] + sqrt(scalaire(a,a))
		
		# On construit la matrice K de la méthode
		K = (2/scalaire(d,d))*(d*numpy.transpose(d))
		
		# Une matrice intermédiare 
		H_int = numpy.eye(n-k) - K
		
		# === Completion de la matrice de Householder ===
		# Avec la matrice identité en haut à gauche 
		H[0:k+1,0:k+1] = numpy.eye(k+1)
		
		# Avec la matrice nulle en bas à gauche 
		H[k:n,0:k] = numpy.zeros([n-k,k])
		
		# Avec la matrice nulle en haut à droite 
		H[0:k, k:n] = numpy.zeros([k,n-k])
		
		# Avec la matrice intermédiaire en bas à droite 
		H[k:n,k:n] = H_int
		
		# On dispose alors de la matrice de Householder pour construire les matrices Q et R
		Q = Q*numpy.transpose(numpy.matrix(H))
		
		R = numpy.matrix(H)*numpy.matrix(R)
		
	# A la sortie de cette boucle on dispose de la décomposition A=QR voulue 
	# On remplace alors b par 
	b = numpy.transpose(Q)*numpy.transpose(numpy.matrix(b)) # A l'entrée de la fonction b est un vecteur ligne
	
	# On remonte le système pour déterminer x 
	x = Remonte(R,b)
	
	return x 
		
# Résolution d'un système tridiagonal
def Tridiagonal(A,b):
	# Ici A est une matrice tridiagonale
	# b est le vecteur solution de Ax=b
	
	# On fixe la taille du systme 
	n = numpy.size(b)
	
	# On déclare les variables de la méthode 
	beta = numpy.zeros([1,n])
	gamma = numpy.zeros([1,n])
	
	# On construit les coefficients beta et gamma 
	beta[0,0] = A[0,0]
	gamma[0,0] = b[0,0]/beta[0,0]
	
	for i in numpy.arange(1,n,1):
		beta[0,i] = A[i,i] - (A[i,i-1]*A[i-1,i])/beta[0,i-1]
		gamma[0,i] = (b[0,i] - A[i,i-1]*gamma[0,i-1])/beta[0,i]
		
	# Les coefficients sont construits 
	
	# On déclare le vecteur solution 
	x = numpy.zeros([1,n])
	
	# On construit la solution 
	x[0,n-1] = gamma[0,n-1] 	
	
	for i in numpy.arange(n-2, -1, -1):
		x[0,i] = gamma[0,i] - (A[i,i+1]*x[0,i+1])/beta[0,i]
		
	return x 
	
	
	
