class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] + [float('inf')]*amount
        x = dp[-1]
        for i in range(1,len(dp)):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i],dp[i-c]+1)
        if dp[-1] == x:
            return -1
        return dp[-1]
