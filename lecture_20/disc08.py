# Q1
""" (define (vir-fib n)
    (cond 
          ((= n 0) 0)
          ((= n 1) 1)
          (else (+ 
                   (vir-fib (- n 1))
                   (vir-fib (- n 2))))
    )
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)
 """

# Q2
""" (define with-list
    (list
        (list 'a 'b) 
        'c 
        'd
        (list 'e)
    )
)
(draw with-list)
 """

""" (define with-quote
    '(
        (a b)
        c
        d
        (e)
    )

)
(draw with-quote)
 """

""" (define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        helpful-list
        another-helpful-list
    )
)
(draw with-cons)
 """

# Q3
""" (define (list-concat a b)
    (cond 
          ((not (null? a)) (cons (car a) (list-concat (cdr a) b)))
          ((null? b) nil)
          (else (cons (car b) (list-concat a (cdr b))))
          )
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))
 """

# Q4
""" (define (map-fn fn lst)
    (if (null? lst) 
        nil
        (cons
            (fn (car lst))
            (map-fn fn (cdr lst))
            )
    )
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)
 """

# Q5
""" (define (remove item lst)
    (if (null? lst)
        nil
        (if (= item (car lst))
            (remove item (cdr lst))
            (cons (car lst) (remove item (cdr lst)))
            )
        )
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))
 """

# Q6
""" (define (duplicate lst)
    (define (helper lst n)
        (cond 
              ((null? lst) nil)
              ((= n 1)
                  (cons (car lst) (helper lst 0))
              )
              (else 
                    (cons (car lst) (helper (cdr lst) 1))
                )
        )
    )
    (helper lst 1)
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))
(expect (duplicate '(1 1)) (1 1 1 1))
 """