"""
Énoncé :
Demander le type de plat (viande, poisson, végétarien).
Si viande → demander cuisson (saignant, à point, bien cuit).
Si poisson → demander sauce (citron, beurre).
Si végétarien → proposer salade ou pâtes.
"""
plat = input("Choisissez un plat (viande/poisson/végétarien) : ").lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant/à point/bien cuit) : ").lower()
    print(f"Vous avez choisi une viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron/beurre) : ").lower()
    print(f"Vous avez choisi un poisson sauce {sauce}.")
elif plat == "végétarien":
    choix = input("Souhaitez-vous une salade ou des pâtes ? ").lower()
    print(f"Vous avez choisi : {choix}.")
else:
    print("Choix invalide.")