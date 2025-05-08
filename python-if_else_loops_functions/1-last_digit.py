#!/usr/bin/python3
import random # Importe le module "random" pour générer des nombres aléatoires
number = random.randint(-10000, 10000)
# Génère un nombre aléatoire entre -10000 et 10000 inclus, stocké dans "number"
last_digit = abs(number) % 10
# Calcule le dernier chiffre du nombre (en valeur absolue pour éviter les problèmes de signe)
# % 10 donne le reste de la division par 10, donc le dernier chiffre
if number < 0:
    last_digit = -last_digit     
    # Si le nombre est négatif, on garde le signe du dernier chiffre pour respecter la valeur réelle
print(f"Last digit of {number} is {last_digit}", end='')
# Affiche le nombre et son dernier chiffre, sans retour à la ligne
if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
# Selon la valeur du dernier chiffre, affiche une information complémentaire