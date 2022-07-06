(module
 (table 0 anyfunc)
 (memory $0 1)
 (export "memory" (memory $0))
 (export "fib" (func $fib))
 (func $fib (; 0 ;) (param $0 i32) (result i32)
  (local $1 i32); local variables declared
  (local $2 i32) 
  (local $3 i32)
  (block $label$0
   (br_if $label$0
    (i32.lt_s
     (get_local $0)
     (i32.const 3); loop skipped if n < 3
    )
   )
   (set_local $0
    (i32.add
     (get_local $0)
     (i32.const -2); compute n - 2
    )
   )
   (set_local $2
    (i32.const 1); next = 1
   )
   (set_local $3
    (i32.const 1)
   )
   (loop $label$1
    (set_local $2
     (i32.add
      (tee_local $1
       (get_local $2)
      )
      (get_local $3)
     )
    )
    (set_local $3
     (get_local $1)
    )
    (br_if $label$1
     (tee_local $0
      (i32.add
       (get_local $0)
       (i32.const -1)
      )
     )
    )
   )
  )
  (get_local $2); the final result
 )
)
