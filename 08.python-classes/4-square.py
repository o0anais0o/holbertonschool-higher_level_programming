#!/usr/bin/python3
"""
Définit une classe Square avec des accesseurs de propriétés (getter et setter).
"""


class Square:
    """Représente un carré avec les méthodes size et area."""

    def __init__(self, size=0):
        """Initialise le carré avec une taille optionnelle."""
        self.size = size  # Déclenche l'accesseur pour validation

    @property
    def size(self):
        """Accesseur pour la taille."""
        return self.__size

    @size.setter
    def size(self, value):
        """Accesseur pour la taille avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Renvoie la surface actuelle du carré."""
        return self.__size ** 2
