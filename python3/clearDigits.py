class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for x in s:
            if x.isdigit() and len(stk) !=0:
                stk.pop()
            else:
                stk.append(x)
        return ''.join(stk) 

