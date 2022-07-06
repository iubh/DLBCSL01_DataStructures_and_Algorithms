class Trie:
    def __init__(self):
        self._top = dict() #Create top level dictionary

    def buildTrie(self,aList):
        for word in aList:
            d = self._top 
            for letter in word:
                if letter not in d:#no entry for letter
                    d[letter] = dict() #create entry
                d = d[letter]#descend subtree by letter

    def searchTrie(self,word):
        d = self._top 
        for letter in word:
            if letter not in d:#no entry for letter
                print("Not Found")
                return False
            d = d[letter]#descend subtree by letter
        print("Match Found")
        return True

    def printTrie(self):
        print(self._top)
aList = ["all","aloud","above","at","about"]
trial = Trie()
trial.buildTrie(aList)
trial.printTrie()
trial.searchTrie("aloud")
trial.searchTrie("albeit")
trial.searchTrie("abo")



