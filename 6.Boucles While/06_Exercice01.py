"""
Énoncé : 
Générer un nombre aléatoire entre 1 et 100. 
L’utilisateur doit deviner jusqu’à trouver le bon nombre. 
Afficher "Trop petit", "Trop grand" ou "Bravo !". 
"""
import random

# Génération d'un nombre aléatoire
nombre_secret = random.randint(1, 100)
essai = None

while essai != nombre_secret:
    essai = int(input("Devine le nombre (1-100) : "))
    if essai < nombre_secret:
        print("Trop petit.")
    elif essai > nombre_secret:
        print("Trop grand.")
    else:
        print("Bravo, tu as trouvé !")