T = int(input())

nums = [1, 2, 3]
dp = [0] * 10001
dp[0] = 1  

for num in nums:
    for j in range(num, 10001):
        dp[j] += dp[j - num]

for _ in range(T):
    n = int(input())
    print(dp[n])
