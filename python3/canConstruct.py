class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = {}
        for i in range(len(magazine)):
            if magazine[i] in dct:
                dct[magazine[i]] +=1
            else:
                dct[magazine[i]] = 1
        for x in ransomNote:
            if x not in dct:
                return False
            if dct[x] == 0:
                return False
            dct[x] -=1
        return True


