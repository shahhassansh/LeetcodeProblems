class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] > secondList[j][1]:
                j+=1
            elif  secondList[j][0] > firstList[i][1]:
                i+=1
            else:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] >secondList[j][1]:
                    j+=1
                elif secondList[j][1] >firstList[i][1]:
                    i+=1
                else:
                    i+=1
                    j+=1
        return res



        
