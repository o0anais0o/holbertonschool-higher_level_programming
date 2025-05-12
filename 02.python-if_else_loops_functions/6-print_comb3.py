#!/usr/bin/python3

for i in range(0, 9):
    # Boucle sur les entiers de 0 à 8 inclus
    for j in range(i + 1, 10):
    # Pour chaque i, boucle sur les entiers de i+1 à 9 inclus
    # Cela garantit que j est toujours supérieur à i, évitant les doublons et répétitions inverses
        print("{}{}".format(i, j), end=", " if i < 8 or j < 9 else "")
        # Affiche la paire de chiffres i et j collés (ex : "01", "12", "89")
        # Ajoute une virgule et un espace après chaque paire sauf la dernière (quand i=8 et j=9)
print()
# Affiche un retour à la ligne à la fin pour que la sortie soit propre