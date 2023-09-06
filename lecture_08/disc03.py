# Q1
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    Hint: 5 * 3 = 5 + (5 * 2) = 5 + 5 + (5 * 1).
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

# Q2   
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2 or n == 1:
        return n
    else:
        return n * skip_mul(n - 2)
    
# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def prime_helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return prime_helper(i+1)
    return prime_helper(2)

# Q5
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    def hailstone_helper(n, k):
        print(n)
        if n == 1:
            return k
        elif n % 2 == 0:
            return hailstone_helper(n // 2, k + 1)
        else:
            return hailstone_helper(n * 3 + 1, k + 1)
    return hailstone_helper(n, 1)

# Q6
def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 <= n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    elif n2 % 10 < n1 % 10:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    
# Q7
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    if n == 1 or n == 2:
        return n
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    
# Q8
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