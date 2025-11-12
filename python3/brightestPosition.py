class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        arr = []
        for a in lights:
            t = a[0]
            arr.append((t - a[1],1))
            arr.append((t + a[1],-1))
        mx = 0
        mx_i = 0
        tmp = 0
        arr.sort(key = lambda x:(x[0], -x[1]))
        for a in arr:
            tmp = tmp+a[1]
            if tmp > mx:
                mx = tmp
                mx_i = a[0]
        return mx_i

        
