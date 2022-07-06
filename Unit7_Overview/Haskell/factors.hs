factors n = [f | f <-[1..n], mod n f == 0]
main = do
print $ factors 60
