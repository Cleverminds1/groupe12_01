"""
Énoncé :
Demander un mot de passe, vérifier :
• ≥ 8 caractères
• Contient au moins un chiffre
• Contient au moins une majuscule
Afficher "Mot de passe valide" ou "Mot de passe invalide".
"""
mdp = input("Entrez un mot de passe : ")
if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")