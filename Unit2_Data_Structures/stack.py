class Stack:
    def __init__(self):
        self.elements = [] #Initialized to an empty list
        
    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)
   
    def topOfStack(self):
        return self.elements[len(self.elements)-1]

    def push(self, newElement):
        self.elements.append(newElement)

    def pop(self):
        return self.elements.pop() #Use Python's in-built pop

def reverse(L):
    s=Stack()
    for i in L:
        s.push(i)
    del L[:]
    n=s.size()
    for j in range(0,n):
        L.append(s.pop())
    print(L)
reverse([1,2,3,4,5,6])
    
    



    
          
    
        
       
    
    
        

