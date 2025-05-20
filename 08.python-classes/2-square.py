#!/usr/bin/python3
"""Définit une classe Square avec validation de taille."""


class Square:
    """Représente un carré avec validation de taille."""

    def __init__(self, size=0):
        """Initialise le carré.

        Arguments :
        size (int) : La taille du carré (doit être >= 0).

        Lève :
        TypeError : Si size n'est pas un entier.
        ValueError : Si size est inférieure à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
