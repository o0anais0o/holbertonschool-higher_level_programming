#!/usr/bin/python3
# Ce script découvre et affiche les noms d'un module caché.

import hidden_4 # L'importation du module

# Ce bloc s'exécute uniquement si le script est lancé directement
if __name__ == "__main__":
    # Obtient la liste de tous les noms définis dans le module hidden_4
    tous_les_noms = dir(hidden_4)

    # Crée une liste pour stocker les noms qui ne commencent pas par "__"
    noms_filtres = []

    # Boucle sur chaque nom trouvé dans le module
    for nom in tous_les_noms:
        # Vérifie si le nom ne commence pas par deux tirets bas
        if not nom.startswith("__"):
            # Si c'est le cas, ajoute le nom |  notre liste filtrée
            noms_filtres.append(nom)

    # Trie la liste des noms filtrés par ordre alphabétique
    # La fonction sorted() retourne une nouvelle liste triée.
    noms_tries = sorted(noms_filtres)

    # Boucle sur chaque nom dans la liste triée et l'affiche
    for nom_final in noms_tries:
        print(nom_final)
        