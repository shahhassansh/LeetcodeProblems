class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dct = {}
        for i in range(len(s)):
            if s[i] in dct:
                dct[s[i]] +=1
            else:
                dct[s[i]] = 1
        st = ''
        for a in order:
            if a in dct:
                for i in range(dct[a]):
                    st = st+a
                dct[a] = 0
        for a in s:
            if dct[a] >0:
                st = st+a
        return st
