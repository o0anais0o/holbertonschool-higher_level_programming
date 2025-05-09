#!/usr/bin/python3

# Ce bloc garantit que le code ne s'exécute que si le script est lancé directement
if __name__ == "__main__":
    # Importe les fonctions add, sub, mul, div du fichier calculator_1.py
    from calculator_1 import add, sub, mul, div
    # Définit la variable a avec la valeur 10
    a = 10
    # Définit la variable b avec la valeur 5
    b = 5
    # Affiche le résultat de l'addition de a et b
    print("{} + {} = {}".format(a, b, add(a, b)))
    # Affiche le résultat de la soustraction de a et b
    print("{} - {} = {}".format(a, b, sub(a, b)))
    # Affiche le résultat de la multiplication de a et b
    print("{} * {} = {}".format(a, b, mul(a, b)))
    # Affiche le résultat de la division de a et b
    print("{} / {} = {}".format(a, b, div(a, b)))
    