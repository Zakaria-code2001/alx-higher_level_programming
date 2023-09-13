#!/usr/bin/python3
"""DEFINES A FILE APPENDING FUNCTION."""


def append_write(filename="", text=""):
    """APPENDS A STRING TO THE END OF A UTF8 TEXT FILE.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
