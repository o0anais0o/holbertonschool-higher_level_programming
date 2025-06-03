#!/usr/bin/python3

def class_to_json(obj):
    """
    Retourne le dictionnaire de description d'un objet
    pour la sérialisation JSON (attributs simples uniquement).
    """
    return obj.__dict__
