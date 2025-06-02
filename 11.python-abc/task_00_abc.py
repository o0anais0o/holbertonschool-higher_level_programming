#!/usr/bin/python3

from abc import ABC, abstractmethod


# Définition de la classe abstraite
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Méthode abstraite à implémenter dans les sous-classes


# Sous-classe Dog
class Dog(Animal):
    def sound(self):
        return "Bark"


# Sous-classe Cat
class Cat(Animal):
    def sound(self):
        return "Meow"


# Exemple d'utilisation
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(dog.sound())  # Affiche : Bark
    print(cat.sound())  # Affiche : Meow
