# task_02_csv.py

import csv   # Module pour lire les fichiers CSV
import json  # Module pour écrire les fichiers JSON


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en un fichier JSON nommé 'data.json'.

    Arguments :
        csv_filename (str): Le nom du fichier CSV à convertir.

    Retourne :
        True si la conversion a réussi, False sinon.
    """
    try:
        # Ouvre le fichier CSV en lecture
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            # Utilise DictReader pour convertir chaque ligne en dictionnaire
            reader = csv.DictReader(csvfile)
            # Convertit l'itérateur en liste de dictionnaires
            data = list(reader)

        # Sérialise la liste de dictionnaires JSON et l'écrit dans 'data.json'
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True  # Conversion réussie

    except Exception as e:
        # En cas d'erreur (fichier non trouvé, etc.), retourne False
        return False


# Exemple d'utilisation (à commenter ou retirer pour usage en import)
if __name__ == "__main__":
    result = convert_csv_to_json("input.csv")
    if result:
        print("Conversion réussie !")
    else:
        print("Erreur lors de la conversion.")
