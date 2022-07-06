part (i:j) = [x|x<-j, x <= i]++[i]++[x|x<-j, x > i]
main = do
print $ part [13, 9, 44, 53, 6, 5, 23, 2, 39]
