#!/usr/bin/python3

def fizzbuzz():
    """
    Affiche les nombres de 1 à 100 avec les règles FizzBuzz,
    séparés par un espace.
    """
    for i in range(1, 101):
        # Si i est un multiple de 3 et de 5, affiche 'FizzBuzz'
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        # Si i est un multiple de 3, affiche 'Fizz'
        elif i % 3 == 0:
            print("Fizz", end=' ')
        # Si i est un multiple de 5, affiche 'Buzz'
        elif i % 5 == 0:
            print("Buzz", end=' ')
        # Sinon, affiche simplement le nombre
        else:
            print(i, end=' ')
