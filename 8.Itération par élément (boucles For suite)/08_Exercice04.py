'''
Énoncé : 
Demander une phrase à l’utilisateur, afficher le nombre de mots ayant plus de 5 lettres. 
'''
phrase = input("Entrez une phrase : ")
mots = phrase.split()

count = 0
for mot in mots:
    if len(mot) > 5:
        count += 1

print(f"Nombre de mots > 5 lettres : {count}")