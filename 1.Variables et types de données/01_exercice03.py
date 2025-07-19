#Énoncé : Écrire un script qui convertit une durée en secondes (entrée sous forme d'heures, minutes, secondes).
heures = int(input("Nombre d'heures : "))
minutes = int(input("Nombre de minutes : "))
secondes = int(input("Nombre de secondes : "))

total_secondes = heures * 3600 + minutes * 60 + secondes

print(f"Durée totale : {total_secondes} secondes.")