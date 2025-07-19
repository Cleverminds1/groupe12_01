"""
Énoncé : 
Demander un nombre à l’utilisateur et afficher sa table de multiplication de 1️ à 1️2️ sous forme 
formatée.
"""

nombre = int(input("Entrez un nombre pour sa table de multiplication : "))

print(f"== Table de {nombre} ==")
for i in range(1, 13):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")