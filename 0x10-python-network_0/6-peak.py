#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list"""
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] >= list_of_integers[mid + 1] and list_of_integers[mid] >= list_of_integers[mid - 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    # If the loop exits, the peak is the last remaining element
    return list_of_integers[left]
