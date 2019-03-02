""" This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element
of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    # With a classical function
    # def first(a, b):
    #     return a
    # return f(first)

    # With a lambda function
    return f(lambda a, b : a)

def cdr(f):
    # With a classical function
    # def last(a, b):
    #     return b
    # return f(first)

    # With a lambda function
    return f(lambda a, b : b)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4