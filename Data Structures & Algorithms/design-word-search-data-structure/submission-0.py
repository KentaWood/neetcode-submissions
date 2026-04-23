class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        
        curr = self.root

        for c in word:

            if c not in curr.children:
                curr.children[c] = Node()

            curr = curr.children[c]
        curr.word = True

        return 

    def search(self, word: str) -> bool:

        stack = [[self.root, 0]]


        while stack:

            node, i = stack.pop()

            if i == len(word):

                if node.word:
                    return True
                
                continue
            c = word[i]

            if c == ".":
                for child in node.children.values():
                    stack.append([child, i + 1])

            else:
                if c in node.children:
                    stack.append([node.children[c], i + 1])
                
                continue
        return False
        
