#!/usr/bin/python3

for i in range(100):
# Boucle sur les entiers de 0 à 99 inclus (range(100) génère 0, 1, ..., 99)
    print("{:02d}".format(i) + (", " if i < 99 else "\n"), end="")
    # "{:02d}" : Affiche le nombre sur deux chiffres, avec un zéro devant si nécessaire (ex : 01, 02, ..., 99)
    # + (", " if i < 99 else "\n") : Ajoute une virgule et un espace après chaque nombre sauf le dernier, où il ajoute un retour à la ligne
    # end="" : Empêche print d'ajouter un retour à la ligne automatique, pour tout afficher sur une seule ligne (sauf le dernier nombre)
