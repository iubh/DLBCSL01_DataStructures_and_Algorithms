class Parallelogram:
    def __init__(self, p, q):
        self.first = p
        self.second = q
        self.third = p
        self.fourth = q
        
    def perimeter(self):
        return(self.first + self.second +\
               self.third+self.fourth)
        


class Rectangle(Parallelogram):
    def __init__(self, p, q):
        super().__init__(p,q)

    def area(self):
        return(self.first*self.second)
        
class Square(Rectangle):
    def __init__(self, p):
        super().__init__(p,p)

    def area(self):
        return(self.first*self.first)


P=Parallelogram(3,4)
print(P.perimeter())

R=Rectangle(3,4)
print(R.perimeter())
print(R.area())

S=Square(5)
print(S.perimeter())
print(S.area())

