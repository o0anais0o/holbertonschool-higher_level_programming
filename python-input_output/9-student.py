#!/usr/bin/python3
"""
Définit une classe Student avec sérialisation en dictionnaire.
"""


class Student:
    """
    Classe qui définit un étudiant par :
    - first_name
    - last_name
    - age
    """

    def __init__(self, first_name, last_name, age):
        # Initialise les attributs de l'étudiant
        self.first_name = first_name  # Prénom de l'étudiant
        self.last_name = last_name    # Nom de famille de l'étudiant
        self.age = age                # Âge de l'étudiant

    def to_json(self):
        """
        Retourne un dictionnaire représentant l'instance Student.
        """
        # Retourne le dictionnaire des attributs pour la sérialisation JSON
        return self.__dict__
