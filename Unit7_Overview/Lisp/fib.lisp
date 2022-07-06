(defun fib (n)
  (if (or (zerop n) (= n 1)) n
    (+ (fib (- n 1)) (fib (- n 2)))))
(print (fib 9))    
