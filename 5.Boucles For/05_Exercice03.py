"""
Énoncé : 
Demander une chaîne à l’utilisateur et construire une nouvelle chaîne inversée à l’aide d’une 
boucle for. 
"""
texte = input("Entrez une chaîne : ")
inverse = ""
for char in texte:
    inverse = char + inverse  # On ajoute chaque caractère devant

print(f"Chaîne inversée : {inverse}")