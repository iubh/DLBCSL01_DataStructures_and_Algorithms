class Heap:
    def __init__(self):
        self._X = []

    def isEmpty(self):
        return self._X == []

    def size(self):
        return len(self._X)

    def _parent(self, i):
        return((i-1)//2)

    def insert(self, newElement):
        #Append at the end
        self._X.append(newElement)
        i = self.size()-1
        #Bubble up
        while(i > 0):
            top = self._parent(i)
            if(self._X[top] < self._X[i]):
                self._X[top],self._X[i] \
                    = self._X[i],self._X[top]
            else:
                break
            i = top

    def _maxChild(self, i):
        if 2*i + 2 >= self.size():
            maxChild = 2*i+1
        elif self._X[2*i+1] > self._X[2*i+2]:
            maxChild = 2*i+1
        else:
            maxChild = 2*i+2
        return(maxChild)


    def extractMax(self):
        #Remove the maximum element from heap and return
        maxElement=self._X.pop(0)
        if(self.size() != 0):
            #Bring last element to front
            lastElement=self._X.pop()
            self._X.insert(0, lastElement)
            #Trickle down
            i = 0
            while(2*i < self.size()-1):
                m = self._maxChild(i)
                if(self._X[m] > self._X[i]):
                    self._X[i],self._X[m] \
                        = self._X[m],self._X[i]
                else:
                    break
                i =m
            return maxElement

    def reportMax(self):
        return(self._X[0])

    def printHeap(self):
            print(self._X)

H=Heap()
H.insert(5)
H.insert(12)
H.insert(9)
H.insert(7)
H.insert(1)
H.insert(8)
H.insert(13)
H.printHeap()
H.extractMax()
H.printHeap()
