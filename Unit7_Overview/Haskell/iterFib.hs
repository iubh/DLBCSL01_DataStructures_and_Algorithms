f a b = a : f b (a + b)
fib = f 0 1
main = do
    print $ take 10 fib
