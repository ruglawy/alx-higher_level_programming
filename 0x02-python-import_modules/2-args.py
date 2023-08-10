#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    if size == 0:
        print("0 arguments.")
        return
    if size == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(size))
    for i in range(size):
        print("{}: {}".format(i + 1, argv[i]))
