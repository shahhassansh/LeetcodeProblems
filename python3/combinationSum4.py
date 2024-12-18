class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0]=1
        for i in range(1,len(dp)):
            for x in nums:
                if i-x >= 0:
                    dp[i] += dp[i-x]
        return dp[target]

