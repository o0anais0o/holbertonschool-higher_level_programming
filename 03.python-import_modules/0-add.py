#!/usr/bin/python3

# Importe la fonction add depuis le fichier add_0.py
from add_0 import add

# Ce bloc s'exécute uniquement si le script est lancé directement,
# et non lorsqu'il est importé comme module.
if __name__ == "__main__":
    # Définit la variable a avec la valeur 1
    a = 1
    # Définit la variable b avec la valeur 2
    b = 2
    # Calcule la somme de a et b en utilisant la fonction add
    result = add(a, b)
    # Affiche le résultat au format demandé : "a + b = result"
    print('{} + {} = {}'.format(a, b, result))
