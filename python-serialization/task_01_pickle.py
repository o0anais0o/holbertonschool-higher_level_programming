#!/usr/bin/python3

import pickle  # Module standard pour la sérialisation d'objets Python


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialise un nouvel objet CustomObject.

        Arguments :
            name (str)       -- Le nom
            age (int)        -- L'âge
            is_student (bool)-- Statut étudiant
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet dans le format demandé.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance courante et l'enregistre
        dans un fichier avec pickle.

        Arguments :
            filename (str) -- Le nom du fichier où sauvegarder l'objet.
        Retourne None en cas d'erreur.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            # En cas d'erreur (ex: permissions, disque plein...), retourne None
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet CustomObject depuis un fichier pickle.

        Arguments :
            filename (str) -- Le nom du fichier à lire.
        Retourne une instance de CustomObject ou None en cas d'erreur.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except Exception as e:
            # En cas d'erreur (fichier inexistant, format incorrect...),
            # retourne None
            return None


# Exemple d'utilisation (à retirer ou commenter pour un usage en module pur)
if __name__ == "__main__":
    obj = CustomObject("John", 25, True)
    obj.serialize("test.pkl")
    loaded = CustomObject.deserialize("test.pkl")
    if loaded:
        loaded.display()
    else:
        print("Erreur lors de la désérialisation.")
