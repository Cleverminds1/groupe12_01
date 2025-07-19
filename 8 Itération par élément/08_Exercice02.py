'''
Énoncé : 
Demander une liste d’éléments et afficher chaque élément avec son indice.
'''
entree = input("Entrez des éléments : ")
liste = entree.split()

for i, elem in enumerate(liste):
    print(f"Indice {i} : {elem}")