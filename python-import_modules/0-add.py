#!/usr/bin/python3

# Ce bloc s'exécute uniquement si le script est lancé directement,
# et non lorsqu'il est importé comme module.
if __name__ == "__main__":
    # Importe la fonction add depuis le fichier add_0.py
    from add_0 import add
    # Définit la variable a avec la valeur 1
    a = 1
    # Définit la variable b avec la valeur 2
    b = 2
    # Affiche le résultat de l'addition sous la forme demandée
    print("{} + {} = {}".format(a, b, add(a, b)))
    