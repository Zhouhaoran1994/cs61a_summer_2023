# https://inst.eecs.berkeley.edu/~cs61a/su23/disc/disc03/#q8-count-k
def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        # count_k(n - 1, k) + count_k(n - 2, k) + ... + count_k(n - k, k)
        total = 0
        for i in range(1, k + 1):
            total += count_k(n - i, k)
        return total
    
# https://inst.eecs.berkeley.edu/~cs61a/su23/disc/disc04/#q6-maximum-path-sum
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return 1
    else:
        return label(t) + max(map(max_path_sum, branches(t)))
    
# https://inst.eecs.berkeley.edu/~cs61a/su23/lab/lab06/#q4-make-repeater
identity = lambda x: x

def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    return accumulate(composer, identity, n, lambda _: func)

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    for i in range(1, n + 1):
        base = combiner(base, term(i))
    return base


# https://inst.eecs.berkeley.edu/~cs61a/su23/lab/lab06/#q6-it-s-always-a-good-prime
def div_by_primes_under(n):
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker

def div_by_primes_under_no_lambda(n):
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f, i):
                def inner(x):
                    return x % i == 0 or f(x)
                return inner
            checker = outer(checker, i)
        i = i + 1
    return checker

# https://inst.eecs.berkeley.edu/~cs61a/su23/lab/lab06/#q12-number-of-trees
def num_trees(n):
    """Returns the number of unique full binary trees with exactly n leaves. E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    if n == 1 or n == 2:
        return 1
    # catalan number
    ans = 0
    for i in range(1, n):
        ans += num_trees(i) * num_trees(n - i)
    return ans

# https://inst.eecs.berkeley.edu/~cs61a/su23/lab/lab07/#q4-sequence-generator
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

# https://inst.eecs.berkeley.edu/~cs61a/su23/lab/lab07/#q5-stair-ways
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

# https://inst.eecs.berkeley.edu/~cs61a/su23/lab/lab07/#q6-church-generator
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
        g = (lambda g: (lambda x: f(g(x))))(g)