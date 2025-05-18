#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Tente de diviser a par b et affiche le résultat.
    Args:
        a: le numérateur
        b: le dénominateur
    Returns:
        Le résultat de la division, ou None si division par zéro.
    """
    try:
        # Tente d'effectuer la division
        res = a / b
        return res
    except ZeroDivisionError:
        # Si division par zéro, assigne None à res
        res = None
        return res
    finally:
        # Affiche toujours le résultat, même en cas d'erreur
        print("Inside result: {}".format(res))
