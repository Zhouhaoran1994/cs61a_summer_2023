from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t) and label(t) in vals:
        return None
    elif is_leaf(t):
        return t
    else:
        new_branches = []
        for b in branches(t):
            if prune_leaves(b, vals):
                new_branches.append(prune_leaves(b, vals))
        return tree(label(t), new_branches)


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    while x > 0:
        last, second_last = x % 10, x // 10 % 10
        if last < second_last:
            return False
        else:
            return ordered_digits(x // 10)
    return True


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while not final:
        while n > 10 and n % 10 > n // 10 % 10:
            n = n // 10
        final = n % 10 if i == k else None
        i += 1
        n = n // 10
    return final

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
    def repeat(x):
        for _ in range(n):
            x = func(x)
        return x
    return repeat

# extra challenge
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

def composing_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = composing_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> composing_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> composing_repeater(square, 2)(5) # square(square(5))
    625
    >>> composing_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> composing_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    return accumulate(composer, identity, n, lambda _: func)

def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    return lambda x: make_repeater(func, 2)(x)

def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________


def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assume that
     nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + e for e in nested_list]


def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    
    # [2, 3]
    # [[], [3]] + [[2], [2, 3]] -> subsets + insert_into_all(s[0], subsets)
   
    if not s:
        return [[]]
    else:
        subsets = subseqs(s[1:])
        return insert_into_all(s[0], subsets) + subsets

def non_decrease_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])
            b = subseq_helper(s[1:], prev)
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, -1)


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
    >>> num_trees(4)
    5
    >>> num_trees(8)
    429

    """
    # 3 = 2+1, 1+2
    # 4 = 3+1, 1+3, 2+2
    # 5 = 4+1, 1+4, 4+1, 1+4, 
    # n = (n-1)+1, 1+(n-1), (n-2)+(1+1), 

    if n == 1 or n == 2:
        return 1
    else:
        total = 0
        for i in range(1, n):
            total = total + num_trees(n-i) * num_trees(i) # 2+1, 1+2 # 3+1, 2+2, 1+3
        return total


def remove_odd_indices(lst, odd):
    """Remove elements of lst that have odd indices. Use recursion!

    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    >>> remove_odd_indices([9, 8, 7, 6, 5, 4, 3], False)
    [8, 6, 4]
    >>> remove_odd_indices([2], False)
    []
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'remove_odd_indices',
    ...       ['While', 'For'])
    True
    """
    if lst:
        if odd:
            kept = lst[0]
            return [kept] + remove_odd_indices(lst[1:], not odd)
        else:
            return remove_odd_indices(lst[1:], not odd)
    else:
        return []


def subset_sum(target, lst):
    """Returns True if it is possible to add some of the integers in lst
    to get target.

    >>> subset_sum(10, [-1, 5, 4, 6])
    True
    >>> subset_sum(4, [5, -2, 12])
    False
    >>> subset_sum(-3, [5, -2, 2, -2, 1])
    True
    >>> subset_sum(0, [-1, -3, 15])     # Sum up none of the numbers to get 0
    True
    """
    if  target == 0:
        return True
    
    subsets = subseqs(lst)
    subsets.remove([])
    return True if target in map(sum, subsets) else False

def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))


def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['H', 'D', 'S', 'C']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    >>> cards[26:30]
    ['7S', '7C', '8H', '8D']
    >>> shuffle(cards)[:12]
    ['AH', '7S', 'AD', '7C', 'AS', '8H', 'AC', '8D', '2H', '8S', '2D', '8C']
    >>> shuffle(shuffle(cards))[:12]
    ['AH', '4D', '7S', '10C', 'AD', '4S', '7C', 'JH', 'AS', '4C', '8H', 'JD']
    >>> cards[:12]  # Should not be changed
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half = len(cards) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(cards[:half][i])
        shuffled.append(cards[half:][i])
    return shuffled


def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    >>> d = [1, 1]
    >>> e = [2]
    >>> trade(d, e)
    'Deal!'
    >>> d
    [2]
    >>> e
    [1, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while m <= len(first) and n <= len(second) and not equal_prefix():
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def interval(a, b):
    """Construct an interval from a to b."""
    assert a <= b, 'Lower bound cannot be greater than upper bound'
    return [a, b]


def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]


def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]


def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]


def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    return add_interval(x, -y)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    reciprocal_y = interval(1 / upper_bound(y), 1 / lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))


def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(2, 4)  # Replace this line!
    r2 = interval(2, 4)  # Replace this line!
    return r1, r2


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    if is_leaf(t):
        return [label(t)]
    total = []
    for b in branches(t):
        total += preorder(b)
    return [label(t)] + total

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    repeat_count = 1
    first = next(t)
    while True:
        n = next(t)
        if first == n:
            repeat_count += 1
        else:
            first = n
            repeat_count = 1
        
        if repeat_count == k:
            return first


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    yield n


def change_abstraction(change):
    """
    For testing purposes.
    >>> change_abstraction(True)
    >>> change_abstraction.changed
    True
    """
    change_abstraction.changed = change


change_abstraction.changed = False


# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
prune_leaves(numbers, (3, 4, 6, 7))