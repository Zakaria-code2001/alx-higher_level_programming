#!/usr/bin/python3
"""Square identification"""


class Square:
    """Square representation"""

    def __init__(self, size=0):
        """Square initialization

        Args:
            size (int): new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
