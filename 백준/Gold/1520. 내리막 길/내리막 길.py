import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == M-1 and y == N-1:
        dp[x][y] = 1
        return 1

    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M  and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))