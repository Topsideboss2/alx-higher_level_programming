#!/usr/bin/python3
""" Finds a peak of unsorted integers of a list """


def find_peak(list_of_integers):
    """ Finds a peak of unsorted integers of a list """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)

    if mid - 1 < 0 and mid + 1 >= length:
        return list_of_integers[mid]

    elif mid - 1 < 0:
        return list_of_integers[mid] if list_of_integers[mid] > list_of_integers[mid + 1] else list_of_integers[mid + 1]

    elif mid + 1 >= length:
        return list_of_integers[mid] if list_of_integers[mid] > list_of_integers[mid - 1] else list_of_integers[mid - 1]

    if list_of_integers[mid - 1] < list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if list_of_integers[mid + 1] > list_of_integers[mid - 1]:
        return find_peak(list_of_integers[mid:])

    return find_peak(list_of_integers[:mid])