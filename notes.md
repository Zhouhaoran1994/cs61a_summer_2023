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

## A Hard Pratice

为什么这个功能可以实现？

因为```(lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)```很巧妙地利用```f```记录了上一个```i```的环境

~~~python
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

# Efficiency

## Exponential Time

指数时间: Incrementing n multiplies time by a constant

$a*b^{n+1}=(a*b^n)*b$

~~~python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
~~~

## Quadratic growth

二次增长: Incrementing n increases time by n times a constant

$a*(n+1)^2=(a*n^2)+a*(2n+1)$

~~~python
def overlap(a, b):
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count
~~~

## Linear growth

线性增长: Incrementing n increases time by a constant

$a*(n+1)=(a*n)+a$

~~~python
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)
~~~

## Logarithmic growth

对数增长: Doubling n only increments time by a constant

$a*ln(2*n)=(a*lnn)+a*ln2$

~~~python
def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)
~~~

# Constant growth

常数增长: Increasing n doesn't affect time

# Object

~~~python
eval(repr(object)) == object
# print(object) == str(object)
~~~

# String representation

the ```print()``` function calls the ```__str__``` method of the object and displays the returned string **with the quotations removed**

while simply calling the object in interactive mode in the interpreter calls the ```__repr__``` method and displays the returned string **with the quotations removed**.

~~~python
>>> a = Rational(1, 2)
>>> str(a)
'1/2'
>>> repr(a)
'Rational(1,2)'
>>> print(a)
1/2
>>> a
Rational(1,2)
~~~

# Scheme

## [Special forms](https://inst.eecs.berkeley.edu/~cs61a/su23/disc/disc08/)

### cond

Just like if-elif-else in Python.

~~~scheme
(cond ((> x 10) (print 'big))
    ((> x 5) (print 'medium))
    (else (print 'small)))

(print
    (cond ((> x 10) 'big)
        ((> x 5) 'medium)
        (else 'small)))
~~~

### begin

It combines multiple expressions into one.

~~~scheme
(cond ((> x 10) (begin (print 'big) (print 'guy))
    (else (begin (print 'small) (print 'fry)))
))
~~~

## List

~~~scheme
scm> (cons 1 (cons 2 nil))
scm> (define s (cons 1 (cons 2 nil)))
scm> (car s)
1
scm> (cdr s)
(2)
scm> (list? s)
#t
scm> (null? s)
#f
scm> (null? nil)
#t
scm> (list 1 2 3 4)
(1 2 3 4)
~~~

## Symbolic Programming

~~~scheme
scm> (define a 1)
scm> (define b 1)
scm> (list a b)
(1 2)
scm>  (list 'a 'b)
(a b)
~~~

## Tail recursion

A tail call occurs when a function calls another function as the last action of the current frame.

~~~scheme
(define (length s)
    (if (null? s) 0
        (+ 1 (length (cdr s))))) ; not a tail call, other works to do

(define (length-tail s)
    (define (length-iter s n)
        (if (null? s) 0
            (length-iter (cdr s) (+ 1 n))))) ; a tail call
~~~

The interpreter needed less steps to come up with the result, and it didn't need to re-visit the earlier frames to come up with the final product.

~~~scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 6)
(* 6 (factorial 5))
(* 6 (* 5 (factorial 4)))
(* 6 (* 5 (* 4 (factorial 3))))
(* 6 (* 5 (* 4 (* 3 (factorial 2)))))
(* 6 (* 5 (* 4 (* 3 (* 2 (factorial 1))))))
(* 6 (* 5 (* 4 (* 3 (* 2 1)))))
(* 6 (* 5 (* 4 (* 3 2))))
(* 6 (* 5 (* 4 6)))
(* 6 (* 5 24))
(* 6 120)
720
~~~

~~~scheme
(define (factorial n)
  (define (fact-tail n result)
    (if (= n 0)
        result
        (fact-tail (- n 1) (* n result))))
  (fact-tail n 1))

(factorial 6)
(fact-tail 6 1)
(fact-tail 5 6)
(fact-tail 4 30)
(fact-tail 3 120)
(fact-tail 2 360)
(fact-tail 1 720)
(fact-tail 0 720)
720
~~~