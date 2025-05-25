class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        for i in range(len(responses)):
            responses[i] = list(set(responses[i]))
        mx = 0
        dct = {}
        for a in responses:
            for b in a:
                if b in dct:
                    dct[b] +=1
                else:
                    dct[b] = 1
                if dct[b] >= mx:
                    if dct[b] > mx:
                        mx = dct[b]
                        res = b
                    else:
                        res = sorted([res,b])
                        res = res[0]
        return res

        
