class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1,str2 = str2, str1
        l1, l2 = len(str1), len(str2)
        for i in range(len(str1), 0, -1):
            if l1 % i != 0 or l2 % i != 0:
                continue
            n1, n2 = l1 / i, l2/i
            pre = str1[:i]
            if pre * int(n1) == str1 and pre * int(n2) == str2:
                return pre
        return ""
