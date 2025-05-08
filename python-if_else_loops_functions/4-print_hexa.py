#!/usr/bin/python3

for i in range(99):
# Boucle sur les entiers de 0 à 98 inclus (range(99) génère 0, 1, ..., 98)
    print("{:d} = 0x{:x}".format(i, i))
    # Affiche chaque entier 'i' en décimal (d) puis en hexadécimal (x) avec le préfixe '0x'
    # Exemple : "42 = 0x2a"