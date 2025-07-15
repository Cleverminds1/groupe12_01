"""
Énoncé :
Demander une note sur 100 et attribuer une mention :
• ≥ 90 : Excellent
• ≥ 75 : Très Bien
• ≥ 60 : Bien
• ≥ 50 : Passable
• < 50 : Insuffisant
"""
note = float(input("Entrez votre note sur 100 : "))

if note >= 90:
    print("Mention : Excellent")
elif note >= 75:
    print("Mention : Très Bien")
elif note >= 60:
    print("Mention : Bien")
elif note >= 50:
    print("Mention : Passable")
else:
    print("Mention : Insuffisant")
