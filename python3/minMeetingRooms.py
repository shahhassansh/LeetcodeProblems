class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []

        for a in intervals:
            times.append((a[0],1))
            times.append((a[1],-1))
        
        times.sort()
        num_rooms = 0
        ans = 0
        for x in times:
            num_rooms = num_rooms + x[1]
            ans = max(ans, num_rooms)
        return ans
        
