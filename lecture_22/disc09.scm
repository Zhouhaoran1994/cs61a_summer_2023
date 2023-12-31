; Q4: Sum
(define (sum lst)
  (define (sum-tail lst result)
    (if (null? lst)
      result
      (sum-tail (cdr lst) (+ (car lst) result))
    )
  )
  (sum-tail lst 0)
)

(expect (sum '(1 2 3)) 6)
(expect (sum '(10 -3 4)) 11)


; Q5: Reverse
(define (reverse lst)
  (define (reverse-tail lst result)
    (if (null? lst)
        result
        (reverse-tail (cdr lst) (cons (car lst) result))
    )
  )
  (reverse-tail lst '())
)

(expect (reverse '(1 2 3)) (3 2 1))
(expect (reverse '(0 9 1 2)) (2 1 9 0))


; Q6: Distance
(define (distance city-a city-b)
    (define (x1 (get-lat city-a)))
    (define (y1 (get-lon city-a)))
    (define (x2 (get-lat city-b)))
    (define (y2 (get-lon city-b)))
    (sqrt
        (+ 
            (expt 
                (- x1 x2)
            )
            (expt 
                (- y1 y2)
            )
        )
    )
)


; Q7: Closer City
(define (closer-city lat lon city-a city-b)
    (define target (make-city 'Target lat lon))
    (define distance-a (distance target city-a))
    (define distance-b (distance target city-b))
    (if (< distance-a distance-b)
        city-a
        city-b
    )
)


; Q8: Is Leaf
(define (is-leaf? t)
    (if (null? (branches t))
        #t
        #f
    )
)


; Q9: Sum Nodes
(define (sum-list lst)
    (define (sum-list-helper lst result)
        (if (null? lst)
            result
            (sum-list-helper (cdr lst) (+ (car lst) result))
        )
    )
    (sum-list-helper lst 0)
)

(expect (sum-list '(1 2 3)) 6)

(define (sum-nodes t)
    (define branch-sums (map sum-nodes (branches t)))
    (if (is-leaf? t)
        (label t)
        (+ branch-sums (label t))
    )
)


; Q10: Fun Tree
(define (fun-tree fun t)
    (define new-label (fun (label t)))
    (define new-branches (map fun (branches t)))
    (tree new-label new-branches)
)
