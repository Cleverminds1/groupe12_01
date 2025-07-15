#Énoncé : Créer une mini "fiche produit" qui contient nom, prix, stock, remise. Calculer le prix final après remise
nom_produit = "casque Bluetooth"
prix = 150.0
stock = 35
remise = 0.15

prix_final = prix * (1 - remise)

print(f"Produit : {nom_produit}")
print(f"Prix initial : {prix} €")
print(f"Remise : {remise * 100}%")
print(f"Prix final : {prix_final:.2f} €")
print(f"Stock disponible : {stock}")