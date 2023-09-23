from tree import *

# Q7
def find_path(t, x):
    """
    >>> simplest = tree(2)
    >>> find_path(simplest, 2)
    [2]
    >>> harder = tree(2, [tree(1), tree(15)])
    >>> find_path(harder, 15)
    [2, 15]
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [x]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path