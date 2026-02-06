class RecentCounter:

    def __init__(self):
        self.q = []
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        cnt = 0 
        x = len(self.q)-1
        if x == -1:
            return cnt
        while self.q[x] >= (t-3000):
            cnt+=1
            x-=1
            if x == -1:
                return cnt
        return cnt 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
