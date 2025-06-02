#!/usr/bin/python3

class VerboseList(list):
    # append : ajoute l’élément puis on affiche le message.
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        # extend : compte le nombre d’éléments ajoutés,
        # étend la liste, puis affiche le message.
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        # remove : affiche le message avant de retirer l’élément
        # (si l’élément n’existe pas, l’exception sera levée après le message).
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        # pop : récupère l’élément à retirer, affiche le message,
        # puis retire l’élément.
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


# --- Tests ---
if __name__ == "__main__":
    vlist = VerboseList()

    vlist.append(10)
    vlist.extend([20, 30])
    vlist.remove(20)
    vlist.pop()
    # Edge case: suppression d'un élément non présent dans la liste
    try:
        vlist.remove(99)
    except ValueError as e:
        print(f"Error: {e}")
    # Edge case: extraire d'une liste vide
    try:
        vlist.pop()
    except IndexError as e:
        print(f"Error: {e}")
