"""Exercise 5.14.3.1
Write a function named is_triangle that takes three integers as arguments,
and that prints either “Yes” or “No”, depending on whether you can or cannot
form a triangle from sticks with the given lengths."""

def is_triangle(a, b, c):
    if a > b+c or b > c+a or c > a+b:
        print('No')
    else:
        print('Yes')

is_triangle(3, 5, 8)

"""Exercise 5.14.3.2
Write a function that prompts the user to input three stick lengths, 
converts them to integers, and uses is_triangle to check whether sticks 
with the given lengths can form a triangle."""

def is_triangle(a, b, c):
    if a > b+c or b > c+a or c > a+b:
        print('No')
    else:
        print('Yes')

def input_sticks():
    a = input("Enter length of a: ")
    b = input("Enter length of b: ")
    c = input("Enter length of c: ")

    is_triangle(int(a), int(b), int(c))

input_sticks()