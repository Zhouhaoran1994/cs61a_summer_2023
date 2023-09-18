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