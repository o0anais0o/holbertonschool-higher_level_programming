#!/usr/bin/python3
"""
Ce module définit la classe Student qui représente un étudiant avec un prénom,
un nom et un âge. Il fournit également une méthode pour obtenir une
représentation sous forme de dictionnaire de l'étudiant,
avec la possibilité de filtrer les attributs.

Classe :    Student : définit un étudiant avec des
            attributs publics et une méthode to_json
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de la classe Student.

        Arguments :
            first_name (str) -- le prénom de l'étudiant
            last_name (str)  -- le nom de famille de l'étudiant
            age (int)        -- l'âge de l'étudiant
        """
        self.first_name = first_name  # Prénom de l'étudiant
        self.last_name = last_name    # Nom de famille de l'étudiant
        self.age = age                # Âge de l'étudiant

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'instance Student.

        Si attrs est une liste de chaînes, seuls les attributs dont le nom
        figure dans cette liste sont inclus dans le dictionnaire retourné.
        Sinon, tous les attributs de l'instance sont inclus.

        Arguments :
            attrs (list, optionnel) : liste de noms d'attributs à inclure

        Retour :
            dict : dictionnaire des attributs sélectionnés de l'étudiant
        """
        if attrs is None:
            # Retourne tous les attributs de l'instance
            return self.__dict__
        else:
            # Retourner uniquement les attributs spécifiés
            # dans attrs s'ils existent
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
