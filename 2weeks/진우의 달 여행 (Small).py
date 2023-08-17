import sys

input = sys.stdin.readline

INF = 1000000
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = grid[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 0) or (j == m - 1 and k == 2):
                dp[i][j][k] = INF
                continue

            if k == 0:
                dp[i][j][k] = grid[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            elif k == 1:
                dp[i][j][k] = grid[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            else:
                dp[i][j][k] = grid[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])
                
result = INF
for j in range(m):
    result = min(result, min(dp[n - 1][j]))

print(result)