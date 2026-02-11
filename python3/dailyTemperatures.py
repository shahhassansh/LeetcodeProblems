class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while len(st) >0 and temperatures[st[-1]] <= temperatures[i]:
                idx = st.pop()
            if len(st) == 0:
                res[i] = 0
            else:
                idx = st[-1]
                res[i] = idx - i
            st.append(i)
            print(st)
        return res


        
