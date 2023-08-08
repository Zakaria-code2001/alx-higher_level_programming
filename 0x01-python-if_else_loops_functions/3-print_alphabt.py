#!/usr/bin/python3
for alphaLetters in range(ord('a'), ord('z')+1):
    if alphaLetters != ord("e") and alphaLetters != ord("q"):
        print("{:c}".format(alphaLetters), end="")
