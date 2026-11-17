class Node:
    def __init__(self, x):
        self.val = x
        self.children = defaultdict(Node)
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = Node("root")
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            node = Node(c)
            curr.children[c] = node
            curr = node
            # print("i:"  + c)
            
        curr.eow = True

        return 

         



    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        

        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        

        return True
        
        