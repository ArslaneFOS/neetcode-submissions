class PrefixTree:

    def __init__(self):
        self.is_end = False
        self.children = {}
        
        

    def insert(self, word: str) -> None:
    
        node : PrefixTree
        if word[0] in self.children:
            node = self.children[word[0]]
        else:
            node = PrefixTree()
        
        
        self.children[word[0]] = node
        if len(word) == 1:
            node.is_end = True
        else:
            node.insert(word[1:])


    def search(self, word: str) -> bool:
        last_node : PrefixTree = self
        for c in word:
            if c not in last_node.children:
                return False

            last_node = last_node.children[c]

        return last_node.is_end

    def startsWith(self, prefix: str) -> bool:
        last_node : PrefixTree = self
        for c in prefix:
            if c not in last_node.children:
                return False

            last_node = last_node.children[c]

        return True
        