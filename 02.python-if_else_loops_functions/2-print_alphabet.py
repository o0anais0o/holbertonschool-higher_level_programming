#!/usr/bin/python3

for alphas in range(97, 123):
    # On commence une boucle "for" qui parcourt les nombres de 97 à 122 inclus (123 non inclus)
    # Dans la table ASCII, les codes de 97 à 122 correspondent aux lettres minuscules de 'a' à 'z'    
    print("{}".format(chr(alphas)), end="")
    # Pour chaque nombre (alphas), on affiche le caractère correspondant grâce à chr()
    # L'option end="" permet de ne pas aller à la ligne après chaque caractère (tout est sur la même ligne)