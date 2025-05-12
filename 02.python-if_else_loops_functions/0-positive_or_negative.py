#!/usr/bin/python3
import random # On importe le module "random" qui permet de générer des nombres aléatoires
number = random.randint(-10, 10)
# On génère un nombre aléatoire entier entre -10 et 10 inclus, qu'on stocke dans la variable "number"

if number > 0:
    print(f"{number} is positive")
    # Si le nombre est strictement supérieur à 0, on affiche qu'il est positif
elif number == 0:
    print(f"{number} is zero")
    # Si le nombre est égal à 0, on affiche qu'il est nul
else:
    print(f"{number} is negative")
    # Sinon (donc s'il est inférieur à 0), on affiche qu'il est négatif