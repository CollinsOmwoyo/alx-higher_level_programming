#!/usr/bin/python3
import sys

args = sys.argv
argc = len(args) - 1

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(argc))

for i in range(1, len(args)):
    print("{}: {}".format(i, args[i]))
