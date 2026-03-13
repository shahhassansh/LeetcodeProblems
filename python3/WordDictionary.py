class WordDictionary:

    def __init__(self):
        self.s = defaultdict(list)
        

    def addWord(self, word: str) -> None:
        self.s[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.s[len(word)]
        for x in self.s[len(word)]:
            if self.isMatch(x,word) == True:
                return True
        return False

    def isMatch(self, word1, word2):
        for i in range(len(word1)):
            if word1[i] != word2[i] and word2[i] != '.':
                return False
        return True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
