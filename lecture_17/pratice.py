def bigs(t):
    """
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4
    """
    def f(a, max_ancestor):
        if a.label > max_ancestor:
            return 1 + sum([f(b, a.label) for b in a.branches])
        else:
            return sum([f(b, max_ancestor) for b in a.branches])
    return f(t, float("-inf"))

def prune(t, n):
    """
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> prune(t, 1)
    >>> print(t)
    3
        2
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)

def tree(label, branches=[]):
    if not branches:
        return [label]
    else:
        return ["(", label] + sum(branches, []) + [")"]

def label(t):
    if len(t) == 1:
        return t[0]
    else:
        assert t[0] == "(", t
        return t[1]

def branches(t):
    if len(t) == 1:
        return []
    opened = 1
    assert t[0] == "("
    current_branch = []
    all_branches = []
    for token in t[2:]:
        if token == "(":
            opened += 1
        elif token == ")":
            opened -= 1
        
        current_branch.append(token)
        if opened == 1:
            all_branches.append(current_branch)
            current_branch = []
    assert opened == 0
    return all_branches

def new_branches(t):
    return t[2:-2]

e = """
(ROOT (S (NP (PRP I))
    (VP (AUX 've)
    (ADVP (RB never))
    (VP (VBN seen) (NP (DT such) (DT a) (JJ cute) (NN kangaroo))))
    (. .)))
""".split("\n")

def read_trees(lines): # more than one tree
    trees = []
    tokens = []
    for line in lines:
        if line.strip():
            tokens.extend(line.replace("(", " ( ").replace(")", " ) ").split())
            if tokens.count("(") == tokens.count(")"):
                trees.append(tokens)
                tokens = []
    return trees

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    def __str__(self, indent="\n "):
        """
        >>> t = Tree(3, [Tree(1), Tree(2)])
        >>> print(t)
        3
            1
            2
        """
        if self.is_leaf():
            return indent + str(self.label)
        else:
            s = ""
            for b in self.branches:
                s += b.__str__(indent+"    ")
            return str(self.label) + s