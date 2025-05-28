#!/usr/bin/python3
""" Définit une classe Rectangle qui hérite de BaseGeometry. """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Initialise un nouveau rectangle avec une largeur et une hauteur.
        Les valeurs sont validées pour être des entiers positifs.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

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
