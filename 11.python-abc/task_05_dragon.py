#!/usr/bin/python3

# Définition des mixins
class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Définition de la classe Dragon qui hérite des deux mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Instanciation et démonstration des capacités du dragon
draco = Dragon()
draco.swim()   # Affiche : The creature swims!
draco.fly()    # Affiche : The creature flies!
draco.roar()   # Affiche : The dragon roars!
