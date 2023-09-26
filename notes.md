# Lambda Expressions
A lambda expression evaluates to a function, called a lambda function. For example, ```lambda y: x + y``` is a lambda expression, and can be read as "a function that takes in one parameter ```y``` and returns ```x + y```."

~~~python
>>> what = lambda x : x + 5
>>> what
<function <lambda> at 0xf3f490>

>>> (lambda y: y + 5)(4)
9
>>> (lambda f, x: f(x))(lambda y: y + 1, 10)
11
~~~

# Currying

converting a function that takes multiple arguments into a chain of functions that each take a single argument.

~~~python
>>> def curried_pow(x):
        def h(y):
            return pow(x, y)
        return h

>>> pow(2, 3)
8
>>> curried_pow(2)(3)
8
~~~

# Decorators

a decorator is identical to:

~~~python
@decorator
def fn(x):
    pass

fn = decorator(fn)
~~~ 

# Short Circuiting

```and``` and ```or``` always return the last thing they evaluate.

~~~python
>>> True and 13
13
>>> -1 or 5
-1
~~~

# Sequence unpacking in For statements
~~~python
pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count += 1
~~~

# Lists
## Operation
~~~python
s = [4, 0, 1]
>>> s * 2
[4, 0, 1, 4, 0, 1]
~~~

## Slicing
~~~python
l = [1, 2, 3, 4]
>>> l[::-1] # Make a reversed copy of the list
[4, 3, 2, 1]
~~~

# Dictionary

The order of items in a dictionary depends on Python version.

1. Python 3.6+, it orders by adding
2. Python 3.5+, items appeared in an arbitrary order

~~~python
d = {"X": 10, "V": 5, "I": 1}
# get all keys
>>> d.keys()
# get all values
>>> d.values()
# get keys and values
>>> d.items()

# contructor
d = [("X", 10), ("V", 5), ("I", 1)]
>>> dict(d)

# get a specific key
>>> d.get("X", "no such key")

# dictionary comprehension
>>> {x:x*x for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
~~~

# Iterator

~~~python
d = {"one": 1, "two": 2}
k = iter(d) # equals to iter(d.keys())
>>> next(k)
"one"
>>> next(k)
"two"

v = iter(d.values())
i = iter(d.items())

d2 = {"one": 1, "two": 2}
k = iter(d)
>>> next(k)
"one"
>>> d2["zero"] = 0
>>> next(k)
RuntimeError
~~~

~~~python
# be careful for for-looping an iterator
ri = iter(range(5))
for i in ri:
    print(i) # it works fine

for i in ri:
    print(i) # prints nothing as it already reached the end
~~~

# Count how many times a function was called

~~~python
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted
~~~

# Memoization

~~~python
def memo(f):
    def memoized(n):
        cache = {}
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
~~~