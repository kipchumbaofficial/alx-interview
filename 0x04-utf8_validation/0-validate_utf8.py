#!/usr/bin/python3
""" ALX interview utf vadidation
"""


def validUTF8(data):
    """ Validates in coming data
    """
    counter = 0

    for bits in data:
        binary = bin(bits).replace('0b', '').rjust(8, '0')[-8:]
        if counter == 0:
            if binary.startswith('110'):
                counter = 1
            if binary.startswith('1110'):
                counter = 2
            if binary.startswith('11110'):
                counter = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            counter -= 1

    if counter != 0:
        return False

    return True
