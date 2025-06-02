#!/usr/bin/python3

class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Instanciation et tests
ff = FlyingFish()
ff.fly()      # Affiche : The flying fish is soaring!
ff.swim()     # Affiche : The flying fish is swimming!
ff.habitat()  # Affiche : The flying fish lives both in water and the sky!

# Affichage de l'ordre de résolution des méthodes (MRO)
print(FlyingFish.mro())
