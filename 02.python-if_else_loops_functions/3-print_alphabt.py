#!/usr/bin/python3

for i in range(97, 123):
    # Boucle sur tous les entiers de 97 à 122 inclus (car range(97, 123))
    # Ces entiers correspondent aux codes ASCII des lettres minuscules 'a' à 'z'
    if i not in [101, 113]:
    # Vérifie que le code ASCII 'i' N'EST PAS 101 (lettre 'e') ni 113 (lettre 'q')
        print("{}".format(chr(i)), end="")
        # Si la condition est vraie, convertit le code ASCII en caractère et l'affiche sur la même ligne (end="")