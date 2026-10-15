class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, i):
            cur = node
            
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.isEnd
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)