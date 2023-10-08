#!/usr/bin/python3
for ch in range(97, 123):
    if chr(ch) is 'q' or chr(ch) is 'e':
        continue
    print("{}".format(chr(ch)), end="")
