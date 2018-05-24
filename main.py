
"""
	=== Français ===
	Auteur : Anthony Gerber-Roth
	Date : Mai 2018 
	Contexte : Stage de 3ème année de licence de Physique 
	But : Réaliser une simulation de la propagation d'une onde électromagnétique dans un plasma froid 
	
	Référence bibTex : 
		@PHDTHESIS{colin2001,
		url = "http://www.theses.fr/2001NAN10181",
		title = "Modélisation d'un réflectomètre mode X en vue de caractériser les fluctuations de densité et de champ magnétique : applications aux signaux de Tore Supra",
		author = "Colin, Muriel",
		year = "2001",
		pages = "1 vol.(IX-220 p.)",
		note = "Thèse de doctorat dirigée par Heuraux, Stéphane Physique des plasmas Nancy 1 2001",
		note = "2001NAN10181",
		}
	
	Licence : Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)  
	
	=== English === 
	Author : Anthony Gerber-Roth
	Date : May 2018
	Context : Bachelor internship 
	Goal : Simulation of electromagnetic wave propagation in plasma
	
	bibTex reference :  
		@PHDTHESIS{colin2001,
		url = "http://www.theses.fr/2001NAN10181",
		title = "Modélisation d'un réflectomètre mode X en vue de caractériser les fluctuations de densité et de champ magnétique : applications aux signaux de Tore Supra",
		author = "Colin, Muriel",
		year = "2001",
		pages = "1 vol.(IX-220 p.)",
		note = "Thèse de doctorat dirigée par Heuraux, Stéphane Physique des plasmas Nancy 1 2001",
		note = "2001NAN10181",
		}
		
	License : Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)  
"""

from EInit import *
from VInit import *
from E import *
from V import *
from matplotlib import pyplot as plt 
import matplotlib.animation as animation 
from nglobal import n 
from Trouvermax import *
from splines import *

# Initialisation des champs E et v 
cE = Esecond()
cv = VInit() 

cEprec = EInit()

# Initialisation du temps 
t = 0 

# On crée deux objets pour le graphique
fig, ax = plt.subplots()

# On définit l'axe des x 
x = numpy.arange(0, n, 1)

# On construit la distribution de omega 
W = numpy.zeros([1,n])

for i in numpy.arange(0,n,1):
	W[0,i] = OmegaPe(i)
	
# Une liste dans laquelle on va mettre les courbes 
lines = []

# On crée une courbe formée initialement du tracé du champ électrique
line, = ax.plot(x, cEprec[1,], color="black")
lines.append(line)

# On crée une courbe destinée à former l'enveloppe
line, = ax.plot(x, cEprec[1,], color="red")
lines.append(line)

# On crée une courbe destinée à accueillir omega_pe
line, = ax.plot(x, W[0,], color="orange")
lines.append(line)

# On définit une fonction qui effectue le calcul des champs et renvoie la nouvelle courbe calculée
def animate(i):
	# On place les variables en global
	global t 
	global cE 
	global cEprec 
	global cv 
	global W
	
	# On passe au temps suivant 
	t = t+1 
	
	# On affiche le compteur
	print("t = ",t)
	
	# On sauvegarde la valeur du champ électrique
	save = cE 
	
	# On calcule la nouvelle valeur du champ électrique
	cE = E(cE, cEprec, cv)
	
	# Le nouveau champ précédent est celui qu'on a sauvegardé précedemment
	cEprec = save 
	
	# On calcule la nouvelle valeur du champ de vitesses 
	cv = v(cv, cEprec, cE)
	
	# On enregistre les max du champ 
	Maxs = TrouverMax(numpy.matrix([numpy.abs(cE[1,]),x]))
	
	y = splines(Maxs,x)
    
    # On modifie la courbe
	lines[1].set_ydata(y)
	lines[0].set_ydata(cE[1,])
	lines[2].set_ydata(W[0,])
	
	# On renvoie la courbe
	return lines

# Une autre fonction nécessaire au fonctionnement de l'animation 
def init():
	for line in lines:
		line.set_ydata(numpy.ma.array(x, mask=True))
    
	return lines
    
# Lancement de l'animation
ani = animation.FuncAnimation(fig, animate, numpy.arange(1, 200), init_func=init,
                              interval=25, blit=True)
# Affichage de l'animation 
plt.show()


