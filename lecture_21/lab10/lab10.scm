(define (make-adder num) (lambda (x) (+ num x)))

(define (composed f g) (lambda (x) (f (g x))))

(define (my-filter pred s) 
  (cond 
    ((null? s) nil)
    ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
    (else (my-filter pred (cdr s))))
  )

(define (exp b n)
  (define (helper b n so-far) 
    (if (= n 0)
      so-far
      (helper b (- n 1) (* b so-far))))
  (helper b n 1))

(define (interleave lst1 lst2)
  (cond 
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else (cons (car lst1) (interleave lst2 (cdr lst1))))))

(define (square n) (* n n))

(define (pow base exp)
  (cond 
    ((= exp 0) 1)
    ((even? exp)
      (square (pow base (/ exp 2))))
    (else 
      (* base (pow base (- exp 1))))
  ))