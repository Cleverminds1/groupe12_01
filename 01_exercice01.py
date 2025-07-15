prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

jours_vecus = age * 365

print("\n== PROFIL UTILISATEUR ==")
print(f"Prénom : {prenom}")
print(f"Age : {age} ans ({jours_vecus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")