#!/usr/bin/python3
"""Définit une classe Square capable de s'imprimer elle-même."""


class Square:
    """
    Représente un carré avec ses méthodes de taille, d'aire et d'impression.
    """

    def __init__(self, size=0):
        """Initialise le carré avec une taille optionnelle."""
        self.size = size

    @property
    def size(self):
        """Obtient la taille actuelle."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Renvoie l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Imprimer le carré en utilisant les caractères '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
