#!/usr/bin/python3

"""Définit la classe Square qui hérite de Rectangle."""

# On importe la classe Rectangle depuis le module 9-rectangle.
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe représentant un carré, héritée de Rectangle."""

    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée.

        Args:
            size (int): La longueur côté du carré doit être un entier positif.
        """
        # Valide que size est un entier positif.
        self.integer_validator("size", size)
        # Initialise le carré comme un rectangle de côtés égaux.
        super().__init__(size, size)
        # Attribut privé pour stocker la taille.
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: Aire du carré.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Retourne une représentation lisible du carré.

        Returns:
            str: Représentation sous la forme [Square] size/size.
        """
        return f"[Square] {self.__size}/{self.__size}"
