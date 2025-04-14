class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        res = []
        k = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[k])
                k+=1
            res.append(temp)
        return res


        
