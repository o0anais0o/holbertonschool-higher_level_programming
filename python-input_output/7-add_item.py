#!/usr/bin/python3
"""
Ce script ajoute tous les arguments à une liste Python et
les sauvegarde dans un fichier JSON.
"""
# Importe le module sys pour accéder aux arguments de la ligne de commande
import sys

# Importe les fonctions de sauvegarde et
# de chargement JSON depuis d'autres scripts
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"  # Nom du fichier où la liste sera sauvegardée

try:
    # Tente de charger la liste existante depuis le fichier JSON
    items = load_from_json_file(filename)
except Exception:
    # Si le fichier n'existe pas ou une erreur survient,
    # initialise une liste vide
    items = []

# Ajoute tous les arguments passés en ligne de commande à la liste
# (sauf le nom du script)
items.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(items, filename)
