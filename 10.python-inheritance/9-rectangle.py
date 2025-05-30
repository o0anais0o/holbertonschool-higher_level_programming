#!/usr/bin/python3
"""Définit une classe Rectangle qui hérite de BaseGeometry."""

# On importe la classe Rectangle du fichier 7-rectangle.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Initialise un nouveau rectangle avec une largeur et une hauteur.
        Les valeurs sont validées pour être des entiers positifs.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        # Vérifie que width est un entier > 0
        self.integer_validator("height", height)
        # Vérifie que height est un entier > 0
        self.__width = width  # Attribut privé pour la largeur
        self.__height = height  # Attribut privé pour la hauteur

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
    """
    Retourne une représentation lisible du rectangle,
    au format [Rectangle] <largeur>/<hauteur>.
    """
    def __repr__(self):
        return self.__str__()
