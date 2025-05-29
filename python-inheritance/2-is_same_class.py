#!/usr/bin/python3

"""
Vérifie si obj est exactement une instance de a_class
et pas une sous-classe.
"""


def is_same_class(obj, a_class):
    return type(obj) is a_class
