'''
Énoncé : 
Demander une liste de nombres à l’utilisateur, trier la liste à l’aide de l’algorithme de tri à bulles 
(bubble sort). 
'''
entree = input("Entrez des nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]

n = len(liste)

for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print(f"Liste triée : {liste}")