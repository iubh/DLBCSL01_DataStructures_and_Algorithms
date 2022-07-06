aList=[11,59,26,17,2,1,25,9,3,15]
pivot=11 
ans=(lambda L,p: list(filter(lambda x: x<= p,L)) + \
      list(filter(lambda x: x> p,L)))(aList,pivot)
print(ans)
