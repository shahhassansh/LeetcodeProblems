class Solution:

    def __init__(self, w: List[int]):
        self.list = []
        s = sum(w)
        for i in range(len(w)):
            r = ceil(w[i]*100.0/s)
            self.list= self.list+[i]*r
        

    def pickIndex(self) -> int:
        return random.choice(self.list)

                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
