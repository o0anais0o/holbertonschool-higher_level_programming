#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        # Crée un itérateur à partir de l'itérable fourni.
        self.iterator = iter(iterable)
        # Compteur d'éléments déjà itérés.
        self.count = 0

    def __iter__(self):
        # L'itérateur se retourne lui-même.
        return self

    def __next__(self):
        # Tente de récupérer le prochain élément.
        try:
            item = next(self.iterator)
            self.count += 1  # Incrémente le compteur.
            return item
        except StopIteration:
            # Si plus d'éléments, relance l'exception pour signaler la fin.
            raise

    def get_count(self):
        # Retourne le nombre d'éléments déjà itérés.
        return self.count


# --- Tests ---
if __name__ == "__main__":
    data = [10, 20, 30, 40]
    it = CountedIterator(data)

    print("Itération manuelle :")
    try:
        print(next(it))  # 10
        print(next(it))  # 20
        print("Éléments parcourus :", it.get_count())  # 2
        print(next(it))  # 30
        print(next(it))  # 40
        print(next(it))  # Provoque StopIteration
    except StopIteration:
        print("Fin de l'itération.")

    # Réinitialisation pour boucle for.
    it = CountedIterator(data)
    print("\nItération avec boucle for :")
    for item in it:
        print(item)
    print("Total parcouru :", it.get_count())
