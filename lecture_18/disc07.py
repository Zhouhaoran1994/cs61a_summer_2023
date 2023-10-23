# Pratice

def add(s, v):
    """
    >>> s = Link(1, Link(5, Link(9)))
    >>> add(s, 5)
    Link(1, Link(5, Link(9)))
    >>> add(s, 3)
    Link(1, Link(3, Link(5, Link(9))))
    >>> add(s, 10)
    Link(1, Link(3, Link(5, Link(9, Link(10)))))
    """
    if s.rest is Link.empty:
        s.rest = Link(v)
    elif v > s.first:
        add(s.rest, v)
    elif v < s.first:
        t = Link(s.first, s.rest)
        s.first = v
        s.rest = t
    return s

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    """ def __repr__(self) -> str:
        if self.is_leaf():
            return f"Tree({self.label})"
        else:
            return f"Tree({self.label}, [{repr(self)}])" """
        
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f"Tree({self.label}{branch_str})"
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# disc07

# Q2: Cumulative Mul
from functools import reduce
from operator import mul

def cumulative_mul(t: Tree):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    >>> otherTree = Tree(2, [Tree(1, [Tree(3), Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> cumulative_mul(otherTree)
    >>> otherTree
    Tree(5040, [Tree(60, [Tree(3), Tree(4), Tree(5)]), Tree(42, [Tree(7)])])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t.label
    else:
        for b in t.branches:
            cumulative_mul(b)
        t.label = reduce(mul, [t.label] + [b.label for b in t.branches])

# Q3: Prune Small
def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest labels.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while len(t.branches) > n:
        largest = max(t.branches, key=lambda t: t.label)
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b, n)



class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'