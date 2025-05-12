#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Args:
        my_list (list): The list in which the element will be replaced.
        idx (int): The index of the element to replace.
        element: The new element to insert at the specified index.

    Returns:
        list: The original list if idx is negative or out of range; 
              otherwise, the modified list with the new element.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
