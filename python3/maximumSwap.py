class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        dct = {}
        for i in range(len(n)):
            dct[n[i]] = i
        print(dct)
        for i in range(len(n)):
            for j in range(9,-1,-1):
                if dct.get(str(j)) and j > int(n[i]) and dct[str(j)] > i:
                    n[i],n[dct[str(j)]] = str(j), n[i]
                    return int(''.join(n))

        return int(''.join(n))
            
                
        
