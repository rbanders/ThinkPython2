def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def do_n(function, n):
    if n <= 0:
        return
    function()
    do_n(function, n-1)

do_n(print_n('Hello', 2), 2)