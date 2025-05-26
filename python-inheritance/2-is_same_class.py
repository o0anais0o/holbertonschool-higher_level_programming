#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Vérifie si obj est exactement une instance de a_class
    et pas une sous-classe.
    """
    return type(obj) is a_class

a = 1
if is_same_class(1, int):
    print(f"{a} is an instance of the class {int.__name__}")
