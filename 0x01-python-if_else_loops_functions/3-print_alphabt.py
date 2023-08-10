#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) is 'e' or chr(i) is 'q':
        continue
    print('{:c}'.format(i), end='')
