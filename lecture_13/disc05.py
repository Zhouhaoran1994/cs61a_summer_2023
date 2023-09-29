# Q3
def filter_iter(iterable, f):
    """
    Generates elements of iterable for which f returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for e in iterable:
        if f(e):
            yield e

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

# Q4
def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    # using yield from
    """
    if n > 1:
        if is_prime(n):
            yield n
        yield from primes_gen(n-1)
    """

    # using for and yield
    for i in range(n - 1):
        if is_prime(n - i):
            yield n - i

def ascending_primes_gen(n):
    """Generates primes in increasing order.
    >>> pg = ascending_primes_gen(7)
    >>> list(pg)
    [2, 3, 5, 7]
    """
    # using for and yield
    """
    for i in range(2, n + 1):
        if is_prime(i):
            yield i
    """

    # using yield from
    def helper(i):
        if i <= n:
            if is_prime(i):
                yield i
            yield from helper(i+1)
    return helper(2)

# Q5
def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    partitioner = lambda x: (x // (10 ** k), x % (10 ** k))
    def best_getter(n):
        assert n > 0
        best_seg = None
        while n > 0:
            n, seg = partitioner(n)
            if not best_seg or score(seg) > score(best_seg):
                best_seg = seg
        return best_seg
    return best_getter

# Q6
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper(count, n):
        if n == 0:
            return count
        else:
            return helper(count + count_digit(n // 10, 10 - n % 10), n // 10)
    return helper(0, n)

def count_digit(n, digit):
    """Return how many times digit appears in n.
    >>> count_digit(55055, 5)
    4
    """
    count = 0
    while n > 0:
        if n % 10 == digit:
            count += 1
        n = n // 10
    return count

# Q7
def make_onion(f, g):
    """
    Write a function make_onion that takes in two one-argument 
    functions, F and G, and returns a function that will take in 
    X, Y, and LIMIT and return True if it is possible to reach Y 
    from X in LIMIT steps or less, via only repeated applications 
    of F and G, and False otherwise.

    >>> add_one = lambda x: x + 1
    >>> mul_by_two = lambda y: y * 2
    >>> can_reach = make_onion(add_one, mul_by_two)
    >>> can_reach(0, 5, 4)      # 5 = add_one(mul_by_two(mul_by_two(add_one(0))))
    True
    >>> can_reach(0, 5, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)      # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)      # Not possible
    False
    """
    def can_reach(x, y, limit):
        if x == y:
            return True
        elif limit == 0:
            return False
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
    return can_reach

# Q8
def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    def helper(weights, values, c):
        if len(weights) == 0:
            return 0
        elif min(weights) > c:
            return 0
        elif weights[0] <= c:
            return values[0] + helper(weights[1:], values[1:], c - weights[0])
        else:
            return helper(weights[1:], values[1:], c)

    possibilities = [helper(weights[i:], values[i:], c) for i in range(len(weights))]
    return max(possibilities)

# Q10
from tree import *

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) and is_leaf(t2):
        return tree(label(t1) + label(t2))
    else:
        if len(branches(t1)) >= len(branches(t2)):
            short, long = t2, t1
        else:
            short, long = t1, t2

        b = []
        short_length = len(branches(short))
        for i in range(short_length):
            b.append(add_trees(branches(short)[i], branches(long)[i]))
        
        b += branches(long)[short_length:]

        return tree(label(t1) + label(t2), b)