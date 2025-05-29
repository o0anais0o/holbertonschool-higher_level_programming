#!/usr/bin/python3

""" Module qui définit la classe Square, héritée de Rectangle. """

# On importe la classe Rectangle du fichier 9-rectangle.py
Rectangle = __import__('9-rectangle').Rectangle


# Définition de la classe Square qui hérite de Rectangle.
class Square(Rectangle):
    """ Classe qui représente un carré, héritant de Rectangle. """
    # Constructeur de Square, prend un seul paramètre : size.
    def __init__(self, size):
        """
        Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré doit être un entier positif.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        # On valide que size est un entier positif grâce à la méthode héritée.
        self.integer_validator("size", size)
        # On initialise la classe parente Rectangle avec size
        # pour la largeur et la hauteur.
        super().__init__(size, size)
        # On stocke la taille dans un attribut privé.
        self.__size = size

    # Méthode pour calculer l'aire du carré.
    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns: int: L'aire du carré.
        """
        # L'aire d'un carré = côté * côté.
        return self.__size * self.__size
