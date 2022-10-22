class DNode:
    def __init__(self, elem = None, prev=None, next=None):
        self.element = elem
        self.prevNode = prev
        self.nextNode = next
    def getElement(self):
        return self.element
    def getPrevNode(self):
        return self.prevNode
    def getNextNode(self):
        return self.nextNode
    def setElement(self, elem):
        self.element = elem
    def setPrevNode(self, elem):
        self.prevNode = elem
    def setNextNode(self, elem):
        self.nextNode = elem


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = DNode(None)
        self.tail = DNode(None)

    def isEmpty(self):
        return (self.length==0)

    def getLength(self):
        return self.length


    def _addNodeIntermediate(self, elem, prev, next):
        #Add element between nodes prev and nextelem
        if self.length == 0:
            node = DNode(elem, self.head, self.tail)
            self.head.nextNode = node
            self.tail.prevNode = node
        else:
            temp = DNode(elem, prev, next)
            prev.setNextNode(temp)
            next.setPrevNode(temp)
        self.length +=1

    def _deleteNodeIntermediate(self, elem):
        #Remove intermediate node from list
        lastNode = elem.getPrevNode()
        nextNode = elem.getNextNode()
        lastNode.setNextNode(nextNode)
        nextNode.setPrevNode(lastNode)
        self.length -=1

    def addNodeFront(self,elem):
       #Add element immediately after head node
       self._addNodeIntermediate(elem, self.head, self.head.nextNode)

    def addNodeEnd(self,elem):
       #Add element immediately before tail node
       self._addNodeIntermediate(elem, self.tail.prevNode, self.tail)







list = DoublyLinkedList()
list.addNodeEnd("33")
list.addNodeFront("1")
list.addNodeEnd("44")
node = list.head
while ( node != list.tail):
    print(node.element)
    node = node.nextNode


