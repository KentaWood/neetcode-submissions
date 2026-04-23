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

            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
            print("i:"  + c)

        curr.eow = True
        print(curr.val,curr.eow)

        return 

         



    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            print(c, curr.eow)
            curr = curr.children[c]
        
        # print(curr.children)
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        

        return True
        
        