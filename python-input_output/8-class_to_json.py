#!/usr/bin/python3
"""
Fonction utilitaire pour obtenir une description d'objet sérialisable en JSON.
"""


def class_to_json(obj):
    """
    Retourne le dictionnaire de description d'un objet
    pour la sérialisation JSON (attributs simples uniquement).
    """
    return obj.__dict__
