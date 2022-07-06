linSearch x (m:y)
 | m < x = linSearch x y
 | m == x = True
 | otherwise = False
main = do
print $ linSearch 21 [2*x+1 | x <-[12,13,17,22,23,25]]
print $ linSearch 21 [2*x+1 | x <-[0,1..]]
print $ linSearch 22 [2*x+1 | x <-[0,1..]]
