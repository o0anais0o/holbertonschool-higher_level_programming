#!/usr/bin/python3
"""Définit une classe Square avec un attribut de taille privé."""


class Square:
    """Représente un carré."""

    def __init__(self, size):
        """Initialise le carré avec un attribut de taille privé."""
        self.__size = size
