class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
    
        # node : PrefixTree
        # if word[0] in self.children:
        #     node = self.children[word[0]]
        # else:
        #     node = PrefixTree()
        
        
        # self.children[word[0]] = node
        # if len(word) == 1:
        #     node.is_end = True
        # else:
        #     node.insert(word[1:])

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_end = True


    def search(self, word: str) -> bool:
        cur : TrieNode = self.root
        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur : TrieNode = self.root
        for c in prefix:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return True
        