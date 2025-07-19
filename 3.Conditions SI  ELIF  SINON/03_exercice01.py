"""
Énoncé :
Demander l'âge et le pays d'une personne, vérifier si elle peut s’inscrire à un programme :
• Doit avoir au moins 18 ans.
• Doit venir du Congo ou du Cameroun.
• Sinon, message adapté.
"""
age = int(input("Entrez votre âge : "))
pays = input("Entrez votre pays : ").lower()

if age >= 18 and (pays == "congo" or pays == "cameroun"):
    print("Inscription autorisée.")
elif age < 18:
    print("Vous êtes trop jeune pour vous inscrire.")
else:
    print("Désolé, programme réservé aux ressortissants du Congo ou Cameroun.")