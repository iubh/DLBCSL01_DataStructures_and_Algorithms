def maximinOf3(x, y, z):
    max3 = max(max(x,y),z)
    min3 = min(min(x,y),z)
    return(max3, min3)
print(maximinOf3(15,23,12))
print(maximinOf3(15,23.1,12.5))
      
