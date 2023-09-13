#!/usr/bin/python3
"""DefinES a FILE WRITING function."""


def write_file(filename="", text=""):
    """WRITE a STRING to A UTF8 tEXT FILE.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        THE NUMBER OF CHARACHTERS WRITTEN.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
