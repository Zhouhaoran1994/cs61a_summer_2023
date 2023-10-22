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