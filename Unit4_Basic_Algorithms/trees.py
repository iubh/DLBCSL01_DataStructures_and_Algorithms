aTree=['A',             #Root
       ['B',            #Left Subtree
        ['D',[],[]],
        []],
       ['C',            #Right Subtree
        ['E',
         ['G',[],[]],
         []],
        ['F',[],[]]
       ]]

def treeRoot(aTree):
    if(aTree):
        return aTree[0]

def leftSubTree(aTree):
    if(aTree):
        return aTree[1]

def rightSubTree(aTree):
    if(aTree):
        return aTree[2]


print(treeRoot(aTree))
print(leftSubTree(aTree))
print(rightSubTree(aTree))

def preorder(aTree):
    if aTree:
        print(treeRoot(aTree))
        preorder(leftSubTree(aTree))
        preorder(rightSubTree(aTree))
        
def inorder(aTree):
    if aTree:
        inorder(leftSubTree(aTree))
        print(treeRoot(aTree))
        inorder(rightSubTree(aTree))        
        
    
def postorder(aTree):
    if aTree:
        postorder(leftSubTree(aTree))
        postorder(rightSubTree(aTree))
        print(treeRoot(aTree))
                
def bfSearch(aTree):
    if aTree:
        qList=[aTree]
        while qList:
            nextNode = qList.pop(0)
            if(nextNode):
                print(treeRoot(nextNode))
                qList.append(leftSubTree(nextNode))
                qList.append(rightSubTree(nextNode))
            
print("\nPREORDER:")
preorder(aTree)

print("\nPOSTORDER:")
postorder(aTree)

print("\nINORDER:")
inorder(aTree)

print("\nBFS:")
bfSearch(aTree)
        
    
    
