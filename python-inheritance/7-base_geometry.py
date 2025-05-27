#!/usr/bin/python3
class BaseGeometry:
    """Classe de base pour la géométrie"""

    def area(self):
        """Lève une exception indiquant que la méthode n'est pas implémentée"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que 'value' est un entier strictement positif.

        Args:
            name (str): Nom de la variable à valider
            value (int): Valeur à vérifier

        Raises:
            TypeError: Si 'value' n'est pas un entier
            ValueError: Si 'value' est ≤ 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
