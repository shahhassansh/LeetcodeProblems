class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(str(num))
        even = []
        odd = []
        for x in s:
            if int(x) % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        e_i = 0
        o_i = 0
        res = []
        for i in range(len(s)):
            if int(s[i])%2 == 0:
                res.append(even[0])
                even.pop(0)
            else:
                res.append(odd[0])
                odd.pop(0)
        return int(''.join(res))
                


        
