#!/usr/bin/python3
"""
Module MyList
Classe qui hérite de list et affiche la liste triée.
"""


class MyList(list):
    """Classe héritant de list avec une méthode print_sorted."""

    def print_sorted(self):
        """Affiche la liste triée (ordre croissant) sans la modifier."""
        print(sorted(self))
