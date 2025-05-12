#!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# Initialise la variable 'str' avec une longue chaîne de caractères décrivant Python

str = str[39:66] + str[106:112] + str[0:6]
# Découpe et concatène des parties de la chaîne :
#   - str[39:66] : extrait les caractères de l'indice 39 à 65 inclus ("object-oriented programming")
#   - str[106:112] : extrait les caractères de l'indice 106 à 111 inclus (" with ")
#   - str[0:6] : extrait les 6 premiers caractères ("Python")
# Le résultat concaténé est assigné de nouveau à 'str'

print(str)
# Affiche le résultat final, qui est la concaténation des extraits choisis
