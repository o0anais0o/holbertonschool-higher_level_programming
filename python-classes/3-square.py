#!/usr/bin/python3
"""Définit une classe Square avec validation de taille et calcul d'aire."""


class Square:
    """Représente un carré avec les méthodes size et area."""

    def __init__(self, size=0):
        """Initialise le carré avec une taille optionnelle.

            Arguments :
            size (int) : Taille du carré (doit être ≥ 0).

            Lève :
            TypeError : Si size n'est pas un entier.
            ValueError : Si size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Renvoie la surface actuelle du carré."""
        return self.__size ** 2
