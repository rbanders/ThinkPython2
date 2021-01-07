import math

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

def input_values():
    a = input("Enter value of a: ")
    b = input("Enter value of b: ")
    c = input("Enter value of c: ")
    n = input("Enter value of n: ")

    check_fermat(int(a), int(b), int(c), int(n))

input_values()
