class Node:
    def __init__(self, elem):
        self.element = elem
        self.nextNode = None
    def getElement(self):
        return self.element
    def getNextNode(self):
        return self.nextNode
    def setElement(self, elem):
        self.element = elem
    def setNextNode(self, elem):
        self.nextNode = elem

anode = Node(22)
print(anode.getElement())


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
    def isEmpty(self):
        return (self.length==0)
    def getLength(self):
        return self.length
    def addNode(self,elem):
        temp=Node(elem)
        temp.setNextNode(self.head)
        self.head=temp
        self.length +=1
          
    def deleteNode(self, elem):
        lastNode = None
        thisNode = self.head
        found = False
        while not found:
            if(thisNode == None):
                break
            if thisNode.getElement() == elem:
                found = True
            else:
                lastNode = thisNode
                thisNode = thisNode.getNextNode()
               
        if(thisNode==None):
            print("Element not in list")
        elif lastNode == None: #head node gets deleted
            self.head = thisNode.getNextNode()
            self.length -=1
        else:
            lastNode.setNextNode(thisNode.getNextNode())
            self.length -=1

    def searchNode(self, elem):
        thisNode = self.head
        found = False
        while ((not found) and (thisNode != None)):
            if thisNode.getElement() == elem:
                found = True
            else:
                thisNode = thisNode.getNextNode()            
        return found

    
    
    
        

