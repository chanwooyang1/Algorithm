N = int(input())
nums = list(map(int, input().split()))

dp = [{} for _ in range(N-1)]
dp[0][nums[0]] = 1


for i in range(1, N-1):
	for val, cnt in dp[i-1].items():
		plus = val + nums[i]
		minus = val - nums[i]
		if 0 <= plus <= 20:
			dp[i][plus] = dp[i].get(plus,0) + cnt

		if 0 <= minus <= 20:
			dp[i][minus] = dp[i].get(minus,0) + cnt
			

target = nums[-1]
print(dp[-1].get(target, -1))