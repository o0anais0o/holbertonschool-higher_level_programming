#!/usr/bin/python3

# Ce bloc garantit que le code ne s'exécute que si le script est lancé directement
if __name__ == "__main__":
    import sys  # Importe sys pour accéder aux arguments de la ligne de commande
    total = 0  # Initialise la variable qui contiendra la somme des arguments
    # Parcourt tous les arguments passés après le nom du script
    for arg in sys.argv[1:]:
        # Convertit chaque argument en entier et l'ajoute au total
        total += int(arg)
    # Affiche la somme totale suivie d'une nouvelle ligne
    print(total)
    