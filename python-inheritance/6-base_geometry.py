#!/usr/bin/python3

""" Module définissant la classe BaseGeometry """


class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Lève une exception indiquant que la méthode n'est pas implémentée"""
        raise Exception("area() is not implemented")
