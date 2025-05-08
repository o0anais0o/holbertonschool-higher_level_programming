#!/usr/bin/python3

str1 = "Holberton"
# Initialise la variable 'str1' avec la chaîne "Holberton"

str2 = "School"
# Initialise la variable 'str2' avec la chaîne "School"

str1 += " " + str2
# Concatène un espace puis la chaîne 'str2' à la fin de 'str1'
# Après cette ligne, 'str1' vaut "Holberton School"

print(f"Welcome to {str1}!")
# Utilise une f-string (format string) pour afficher la phrase "Welcome to Holberton School!"
# La valeur de 'str1' est insérée dans la chaîne à l'endroit de {str1}
