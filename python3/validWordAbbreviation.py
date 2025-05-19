class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        prev = -1
        i = 0
        for a in abbr:
            if i>= len(word):
                return False
            if a in '1234567890':
                if prev == -1:
                    if a == '0':
                        return False
                    prev = int(a)
                else:
                    x = str(prev)+str(a)
                    prev = int(x)
            else:
                if prev == -1:
                    if word[i] != a:
                        return False
                    i+=1
                else:
                    i+=prev
                    prev = -1
                    if i >= len(word):
                        return False
                    if word[i] != a:
                        return False
                    i+=1
        if prev == -1:
            if i == len(word):
                return True
            else:
                return False

        if prev == len(word)-i:
            return True
        else:
            return False






        
