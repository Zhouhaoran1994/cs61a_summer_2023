# Prime factorization
# python3 -m doctest prime_factors.py
def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k

def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k

# Boolean contexts

bool(2)
bool(0)
if 2:
    print('hi')

if '': 
    print('hi')
bool('')
bool(' ')
not 2
not 0

# Control

def if_(c, t, f):
    if c:
        return t
    else:
        return f

def error_div(n , d):
    """
    Returns the result of dividing n by d.
    If d is 0, instead return 0
    >>> error_div(100, 10)
    10
    >>> error_div(100, 0)
    0
    """
    return if_(d==0, 0, n//d) # ERRORS
    if d == 0:
        return 0
    else:
        return n // d



# Functions as arguments

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

summation(1000000, pi_term)

# Functional arguments

def apply_twice(f, x):
    """Return f(f(x))

    >>> apply_twice(square, 2)
    16
    >>> from math import sqrt
    >>> apply_twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 2)

# Functional return values

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# This expression causes an error because y is not bound in g.
# f(1, 2)

# Composition

def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
tripare = compose1(triple, square)
squadder = compose1(square, make_adder(2))
squsquadder = compose1(square, squadder)
# Lambda expressions

x = 10
square = x * x
square = lambda x: x * x
square(4)

lambda f,g: lambda x: f(g(x))

def outer(x):
    def inner(y):
        def innerinner(z):
            return z
        return innerinner
    return inner