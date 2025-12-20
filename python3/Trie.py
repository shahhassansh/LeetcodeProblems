class Trie:

    def __init__(self):
        self.s = set()
        

    def insert(self, word: str) -> None:
        self.s.add(word)
        

    def search(self, word: str) -> bool:
        if word in self.s:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        for a in self.s:
            if a[:l] == prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
