#!/usr/bin/python3  
for Numbers in range(0, 100):
    if Numbers == 99:
        print(Numbers)
    else:
        print("{:02d}".format(Numbers), end=", ")
