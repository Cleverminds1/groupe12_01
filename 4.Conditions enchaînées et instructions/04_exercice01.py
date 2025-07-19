"""
Énoncé :
Demander l’âge et la situation (étudiant, salarié, retraité).
Déterminer le tarif :
• Moins de 18 ans → 5 €
• 18-25 ans → étudiant : 6 €, salarié : 8 €
• Plus de 22 ans → retraité : 7 €, sinon 10 €
"""
age = int(input("Age : "))
statut = input("Statut (étudiant/salarié/retraité) : ").lower()

if age < 18:
    tarif = 5
else:
    if 18 <= age <= 25:
        if statut == "étudiant":
            tarif = 6
        elif statut == "salarié":
            tarif = 8
        else:
            tarif = 10
    else:
        if statut == "retraité":
            tarif = 7
        else:
            tarif = 10

print(f"Votre tarif est de {tarif} €.")