#!/usr/bin/python3

word = "Holberton"
# Initialise la variable 'word' avec la chaîne "Holberton"

word_first_3 = word[:3]
# Récupère les 3 premiers caractères de 'word' (du début jusqu'à l'indice 3 non inclus)
# Résultat : "Hol"

word_last_2 = word[-2:]
# Récupère les 2 derniers caractères de 'word' (du 2ème caractère avant la fin jusqu'à la fin)
# Résultat : "on"

middle_word = word[1:-1]
# Récupère la partie centrale de 'word' (du 2ème caractère jusqu'à l'avant-dernier inclus)
# Résultat : "olberto"

print(f"First 3 letters: {word_first_3}")
# Affiche "First 3 letters: Hol"

print(f"Last 2 letters: {word_last_2}")
# Affiche "Last 2 letters: on"

print(f"Middle word: {middle_word}")
# Affiche "Middle word: olberto"
