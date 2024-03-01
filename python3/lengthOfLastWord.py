class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        word = s[len(s)-1]
        return len(word)
