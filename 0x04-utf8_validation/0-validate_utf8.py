#!/usr/bin/python3
'''UTF-8 validation module
'''


def validUTF8(data):
    '''validUTF8:
        returns true if data is a valid UTF-8 else false
    '''
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        if byte > 255:
            return False
        mask = 1 << 7

        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
