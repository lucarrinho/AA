from sys import stdin

n, x = map(int, stdin.readline().split())
coins = list(map(int, stdin.readline().split())).sort()
for i in range(n):
    if coins[i] > x:
        coins = coins[:i]
        break

dp = [float('inf')]*(x+1)
dp[0] = 0

for i in range(1, x+1):
    for moeda in coins:
        if i - moeda >= 0:
            dp[i] = min(dp[i], 1 + dp[i - moeda])

if dp[x] == float('inf'):
    print(-1)
else:
    print(dp[x])