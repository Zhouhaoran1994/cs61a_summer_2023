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