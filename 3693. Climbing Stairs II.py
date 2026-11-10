class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            cost = costs[i - 1]
            dp[i] = float('inf')

            for jump in range(1, 4):
                if i - jump >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i - jump] + cost + jump * jump
                    )

        return dp[n]