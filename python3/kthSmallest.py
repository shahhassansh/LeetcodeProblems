class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hp = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(hp, matrix[i][j])
        cnt = 0
        while cnt < k-1:
            heappop(hp)
            cnt+=1
        return hp[0]
        

        
