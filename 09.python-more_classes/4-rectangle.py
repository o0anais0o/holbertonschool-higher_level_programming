#!/usr/bin/python3
"""
Ce module définit une classe Rectangle qui représente un rectangle.
"""


class Rectangle:
    """ Une classe Rectangle qui définit un rectangle"""

    def __init__(self, width=0, height=0):
        """
        Une classe qui définit un rectangle par sa hauteur et sa largeur.

        Remarque :
        La méthode __init__ attribue des valeurs aux propriétés de l'objet.
        width est un attribut d'instance privé.
        height est un attribut d'instance privé.

        Attributs :
        width (int) : largeur du rectangle.
        height (int) : hauteur du rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Méthode d'obtention de l'attribut width.
        La propriété getter récupère la largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Méthode de définition de l'attribut width.
        Assure que la valeur est un entier >= 0
        """

        # Vérifie si la largeur est un entier
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Vérifie si la largeur est positive
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter pour l'attribut height
        La propriété getter récupère la hauteur du rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter pour l'attribut height.
        Assure que la valeur est un entier >= 0
        """

        # Vérifie si la hauteur est un entier
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # Vérifie si la hauteur est positive
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calcule et renvoie l'aire du rectangle.

        Remarque :
        area est une méthode d'instance publique.

        Retourne :
        int : aire (largeur * hauteur)
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule et renvoie le périmètre du rectangle.

        Remarque :
        perimeter est une méthode d'instance publique.

        Retourne :
        int : périmètre (largeur + hauteur) * 2
        """

        if self.__width == 0 or self.__height == 0:
            result = 0
            return result
        else:
            result = (self.__width + self.__height) * 2
            return result

    def __str__(self):
        """
        Renvoie la représentation sous forme de chaîne du rectangle
        pour l'impression avec « # ». Caractères.

        Remarque :
        __str__ est une méthode spéciale utilisée par print() et str().

        Renvoie :
        str : représentation visuelle du rectangle avec des caractères « # ».
        Renvoie une chaîne vide si la largeur ou la hauteur est égale à 0.
        """

        # Vérifie si la largeur ou la hauteur
        if self.width == 0 or self.height == 0:
            return ""
        # Construire le rectangle ligne par ligne :
        # ('#' * self.width + '\n') * (self.height - 1) :
        # crée toutes les lignes
        # sauf la dernière, chacune se terminant par un saut de ligne.
        # Le dernier + '#'*self.width :
        # ajoute la dernière ligne sans saut de ligne
        # pour éviter une ligne vide supplémentaire à la fin.
        return ('#' * self.width + '\n') * (self.height - 1) + '#' * self.width

    def __repr__(self):
        """
        Renvoie la représentation officielle du rectangle sous forme de chaîne.

        Remarque :
        __repr__ méthode spéciale utilisée pour débogage et développeurs.

        Renvoie :
        str : une chaîne permettant de recréer l'objet avec eval(), au format :
        ClassName(width, height)
        """

        # Renvoie « class_name object(width, height » dans la sortie
        return (f"{self.__class__.__name__}{self.width, self.height}")
