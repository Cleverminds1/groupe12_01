"""
Énoncé :
Demander la valeur d'un panier. Si le montant est :
• ≥ 100 € → Livraison gratuite.
• Entre 50 € et 99.99 € → Livraison 5 €.
• < 50 € → Livraison 10 €.
Afficher le total à payer (panier + livraison).
"""
panier = float(input("Montant du panier (€) : "))

if panier >= 100:
    frais = 0
elif panier >= 50:
    frais = 5
else:
    frais = 10

total = panier + frais
print(f"Frais de livraison : {frais} €")
print(f"Total à payer : {total:.2f} €")