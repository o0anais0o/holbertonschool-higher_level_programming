#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML et l'enregistre dans un fichier.

    Arguments :
        dictionary (dict) -- Le dictionnaire à sérialiser.
        filename (str)    -- Le nom du fichier XML de sortie.
    """
    try:
        root = ET.Element('data')  # Élément racine

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        return False


def _convert_type(value):
    """
    Essaie de convertir la chaîne en int, float, bool ou laisse en str.
    """
    if value is None:
        return None
    value = value.strip()
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value  # Retourne la chaîne si aucune conversion n'est possible


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Arguments :
        filename (str) -- Le nom du fichier XML à lire.

    Retourne :
        dict -- Le dictionnaire reconstruit à partir du XML.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = _convert_type(child.text)
        return result
    except Exception as e:
        return None


# Exemple d'utilisation (à commenter ou retirer pour usage en import)
if __name__ == "__main__":
    data = {
        "name": "Alice",
        "age": 30,
        "height": 1.68,
        "is_student": False
    }
    serialize_to_xml(data, "data.xml")
    loaded = deserialize_from_xml("data.xml")
    print(loaded)
