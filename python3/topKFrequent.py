class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for x in nums:
            if x not in dct:
                dct[x] =1
            else:
                dct[x]+=1
        dct = dict(sorted(dct.items(), key = lambda item:item[1], reverse=True))
        a = list(dct.keys())[:k]
        return a
        
        
        
