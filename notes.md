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