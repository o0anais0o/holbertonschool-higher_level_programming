#!/usr/bin/python3

""" 
Fonction lookup qui retourne la liste des attributs et méthodes d’un objet.
"""


def lookup(obj):
    """Renvoie la liste des attributs et méthodes disponibles d'un objet."""
    return dir(obj)
