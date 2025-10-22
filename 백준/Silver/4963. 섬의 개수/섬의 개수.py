import sys
sys.setrecursionlimit(10**6)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    sea_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    dx = [0, 0, 1, -1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]
    
    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if sea_map[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx, ny)
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if sea_map[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)