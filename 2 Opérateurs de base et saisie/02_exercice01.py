"""
Énoncé :
Écrire un programme qui demande deux nombres à l’utilisateur et affiche :
• Leur somme
• Leur différence
• Leur produit
• Leur quotient (division réelle)
• Leur division entière
• Leur reste (modulo)
"""
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b != 0 else "Division par zéro"
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != 0 else "Division par zéro"

print(f"Somme : {somme}")
print(f"Différence : {difference}")
print(f"Produit : {produit}")
print(f"Quotient : {quotient}")
print(f"Division entière : {division_entiere}")
print(f"Reste : {reste}")