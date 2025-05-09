#!/usr/bin/python3

# Le code s'exécute seulement si le script est lancé directement
if __name__ == "__main__":
    import sys  # Pour accéder aux arguments de la ligne de commande
    total = 0  # Initialise la somme des arguments
    # Parcourt les arguments après le nom du script
    for arg in sys.argv[1:]:
        # Convertit l'argument en entier et l'ajoute au total
        total += int(arg)
    # Affiche la somme totale
    print(total)
    