#!/usr/bin/python3
"""Définit une classe Square avec taille et position."""


class Square:
    """Représente un carré avec taille et position pour l'impression."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise le carré avec taille et position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter pour la taille."""
        return self.__size

    @size.setter
    def size(self, value):
        """Getter pour la taille avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter pour position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter pour la position avec validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Renvoie l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Imprime le carré en utilisant '#' et gère le décalage de position"""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
