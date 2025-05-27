#!/usr/bin/python3
"""Module définissant la classe Rectangle qui hérite de BaseGeometry."""


class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Lève une exception indiquant que la méthode n'est pas implémentée"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que 'value' est un entier strictement positif."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Classe Rectangle, héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise un rectangle avec largeur et hauteur validées."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
