#!/usr/bin/python3
from add_0 import add

def main():
#variables a and b
a = 1
b = 2

# print function with string formatting
print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
main()
