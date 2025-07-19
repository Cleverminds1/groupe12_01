"""
Énoncé :
Demander la température et conseiller :
• ≥ 35°C : "Très chaud, restez hydraté."
• Entre 25 et 34 : "Chaud, faites attention au soleil."
• Entre 15 et 24 : "Température agréable."
• < 15 : "Il fait frais, couvrez-vous."

"""
temp = float(input("Température (°C) : "))

if temp >= 35:
    print("Très chaud, restez hydraté.")
elif temp >= 25:
    print("Chaud, faites attention au soleil.")
elif temp >= 15:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")