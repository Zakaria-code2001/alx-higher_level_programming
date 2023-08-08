#!/usr/bin/python3  
for alphaLetters in range(ord('a'), ord('z')+1):
    if alphaLetters == 'e' or alphaLetters == 'q':
        continue
    else:
        print("{:c}".format(alphaLetters), end="")
