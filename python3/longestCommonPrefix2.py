class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()

        for a in arr1:
            a = str(a)
            prefix = ""
            for x in a:
                prefix +=x
                s.add(prefix)
        mx = 0
        for b in arr2:
            b = str(b)
            prefix = ""
            for y in b:
                prefix +=y
                if prefix in s:
                    mx = max(mx, len(prefix))
        return mx

        
