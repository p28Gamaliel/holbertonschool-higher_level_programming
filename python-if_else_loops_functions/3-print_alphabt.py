#!/usr/bin/python3
for num_ascii in range(ord('a'), ord('z') + 1):
    if chr(num_ascii) != 'e' and chr(num_ascii) != 'q':
        print("{}".format(chr(num_ascii)), end="")
