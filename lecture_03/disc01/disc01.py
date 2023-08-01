# Q1: Case Conundrum
def special_case():
    """
    What is the result of evaluating the following code?

    >>> special_case()
    12
    """
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

def just_in_case():
    """
    What is the result of evaluating this piece of code?

    >>> just_in_case()
    19
    """
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

def case_in_point():
    """
    How about this piece of code?

    >>> case_in_point()
    12
    """
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

# Q2: Jacket Weather?
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp <= 60 or raining:
        return True
    else:
        return False

# Q2 Alternate Solution
def wears_jacket_alt(temp, raining):
    return temp < 60 or raining

# Q3: Nearest Ten
def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    >>> nearest_ten(14)
    10
    """
    if n % 10 < 5:
        return n // 10 * 10
    else:
        return (n // 10 + 1) * 10

# Q3 Alternate Solution
def nearest_ten(n):
    return (n + 5) // 10 * 10

# Q4: Square So Slow
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    """
    What is the result of evaluating the following code?
    
    >it causes an infinite loop.
    """
    x = num
    while x > 0:
        x = x + 1
    return x / 0

# Q5: Is Prime? (质数)
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False

    dividend = 2
    while dividend < n:
        if n % dividend == 0:
            return False
        dividend += 1
    return True

# Q6: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1

# Q7: Unique Digits
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    count = 0
    while n > 0:
        if not has_digit(n // 10, n % 10):
            count += 1
        n = n // 10
    return count

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False


# Q7 Alternate solution
def unique_digits_alt(n):
    unique = 0
    i = 0
    while i < 10:
        if has_digit(n, i):
            unique += 1
        i += 1
    return unique