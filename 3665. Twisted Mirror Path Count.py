class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move right
                r, c = i, j + 1
                direction = 0  # 0 = right, 1 = down

                while r < m and c < n and grid[r][c] == 1:
                    if direction == 0:
                        direction = 1
                        r += 1
                    else:
                        direction = 0
                        c += 1

                if r < m and c < n:
                    dp[r][c] = (dp[r][c] + ways) % MOD

                # Move down
                r, c = i + 1, j
                direction = 1  # 0 = right, 1 = down

                while r < m and c < n and grid[r][c] == 1:
                    if direction == 0:
                        direction = 1
                        r += 1
                    else:
                        direction = 0
                        c += 1

                if r < m and c < n:
                    dp[r][c] = (dp[r][c] + ways) % MOD

        return dp[m - 1][n - 1]