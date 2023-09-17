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