#!/usr/bin/python3
"""Module définissant la classe Rectangle qui hérite de BaseGeometry."""

# On importe la classe Rectangle du fichier 7-rectangle.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle, héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise un rectangle avec largeur et hauteur validées."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
