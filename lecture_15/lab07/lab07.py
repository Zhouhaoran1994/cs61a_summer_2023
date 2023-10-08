LAB_SOURCE_FILE = __file__


def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 3, 2)
    3
    >>> next(s)
    1
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    count = 0
    for _ in range(n):
        if next(t) == x:
            count += 1
    return count


def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that are all true values
    
    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    if x:
        yield x
        yield from amplify(f, f(x))


def sequence_gen(term):
    """
    Yields term(1), term(2), term(3), ...

    >>> s1 = sequence_gen(lambda x: x**2)
    >>> [next(s1) for _ in range(5)]
    [1, 4, 9, 16, 25]
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'sequence_gen',
    ...       ['While', 'For'])
    True
    """
    yield term(1)
    yield from sequence_gen(lambda x: term(x + 1))

def stair_ways(n):
    """
    Yields all ways to climb a set of N stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> try: # Ensure you're not yielding extra
    ...     next(s_w)
    ...     assert False
    ... except StopIteration:
    ...     pass
    """
    if n == 0:
        yield []
    elif n == 1:
        yield [1]
    else:
        for way in stair_ways(n - 1):
            yield way + [1]
        for way in stair_ways(n - 2):
            yield way + [2]
    


def church_generator(f):
    """Takes in a function f and yields functions which apply f
    to their argument one more time than the previously generated
    function.

    >>> increment = lambda x: x + 1
    >>> church = church_generator(increment)
    >>> for _ in range(5):
    ...     fn = next(church)
    ...     print(fn(0))
    0
    1
    2
    3
    4
    """
    g = lambda x: x
    while True:
        yield g
        g = (lambda g: lambda x: g(f(x)))(g)
        # g = lambda x: f(x)
        # lambda x: g(f(x))

# while True:
#   checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
# term = lambda x: term(x+1)