class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dct = {}
        for i in range(len(names)):
            dct[heights[i]] = names[i]
        
        sorted_dct = dict(sorted(dct.items(), key = lambda item : item[0], reverse= True))
        return list(sorted_dct.values())
