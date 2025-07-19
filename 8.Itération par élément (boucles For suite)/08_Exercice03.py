'''
Énoncé : 
Créer une "matrice" 3×3 (liste de listes) et afficher chaque ligne et chaque élément. 
'''
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()  # saut de ligne après chaque ligne