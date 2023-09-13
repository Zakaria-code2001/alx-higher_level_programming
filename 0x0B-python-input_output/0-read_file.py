#!/usr/bin/python3
"""DefiNes a teXt fiLe-reading fuNction."""


def read_file(filename=""):
    """PrInt the conTents oF a UTF8 tExt fIle to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
