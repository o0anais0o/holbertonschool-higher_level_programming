#!/usr/bin/env python3

import json  # Import du module standard pour la gestion du JSON


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    Arguments :
        data (dict) :    Le dictionnaire à sérialiser.
        filename (str) : Le nom du fichier de sortie.
                         Si le fichier existe, il sera remplacé.
    """

    # Ouvre le fichier en mode écriture ('w'), l'encodage est défini sur UTF-8
    with open(filename, 'w', encoding='utf-8') as f:
        # Sérialise le dictionnaire 'data' et
        # l'écrit dans le fichier au format JSON
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et le désérialise en dictionnaire Python.

    Arguments :
        filename (str)   -- Le nom du fichier JSON à lire.

    Retour :
        dict -- Le dictionnaire Python obtenu à partir du fichier JSON.
    """
    # Ouvre le fichier en mode lecture ('r'), l'encodage est défini sur UTF-8
    with open(filename, 'r', encoding='utf-8') as f:
        # Charge le contenu JSON du fichier et
        # le convertit en dictionnaire Python
        return json.load(f)
