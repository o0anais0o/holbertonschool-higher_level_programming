#!/usr/bin/python3
"""
Ce module fournit une fonction pour sauvegarder un objet Python
dans un fichier au format JSON.

Fonction :
    save_to_json_file(my_obj, filename):
        Sérialise un objet Python et l'écrit dans un fichier
        texte au format JSON.
"""


import json  # Importe le module json pour la sérialisation


def save_to_json_file(my_obj, filename):
    """
    Sérialise un objet Python et l'écrit dans un fichier texte au format JSON.

    Args:
        my_obj (object): L'objet Python à sérialiser
        (ex : dictionnaire, liste, etc.).
        filename (str): Le chemin du fichier où écrire la chaîne JSON.

    Raises:
        TypeError: Si l'objet n'est pas sérialisable en JSON.
        Exception: Si l'écriture dans le fichier échoue.
    """
    # Ouvre le fichier en mode écriture ("w")
    with open(filename, "w") as f:
        # Convertit l'objet Python en une chaîne JSON
        json_string = json.dumps(my_obj)
        # Écrit la chaîne JSON dans le fichier
        f.write(json_string)
