# Exercise 1

def right_justify(s):
    space = '     '
    print(space*13 + s)

right_justify('monty')

# Exercise 2.1

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)
print(' ')

# Exercise 2.2-2.4

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print, 'spam')
print(' ')

# Exercise 2.5

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print, 'spam')

# Exercise 3.1

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
print(' ')

# Exercise 3.2

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_four(print_beam)
    print('+')

def print_posts():
    do_four(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_four(print_row)
    print_beams()

print_grid()