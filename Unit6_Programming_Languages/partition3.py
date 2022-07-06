class Scores:
    def __init__(self,L):
        self.S = L

    def part(self,p):
        i=0
        j=self.size()-1
        while True:
            while (i <= j) and (self.S[i] <= p):
                i+=1
            while (i <=j) and (self.S[j] > p):
                j-=1
            if(i <= j):
                self.S[i],self.S[j] = self.S[j],self.S[i]
            else:
                break
        self.S[0],self.S[j]= self.S[j],self.S[0]
        return self.S

    def isEmpty(self):
        return self.S == []
    
    def size(self):
        return len(self.S)
bList =Scores([11,59,26,17,2,1,25,9,3,15])
print(bList.part(11))
