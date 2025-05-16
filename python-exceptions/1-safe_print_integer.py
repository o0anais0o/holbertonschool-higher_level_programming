#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Essayer de formater et d'afficher la valeur comme un entier
        print("{:d}".format(value))
        # Si les lignes ci-dessus s'exécutent sans erreur,
        # cela signifie que 'value' a été traitée comme un entier.
        return True
    except (ValueError, TypeError):  # Ou plus généralement "except Exception:"
        # Si une ValueError (ex: format("hello")) ou TypeError (ex: format([]))
        # se produit lors du formatage, on arrive ici.
        # (La question de l'affichage sur stderr reste si sys est interdit)
        return False
