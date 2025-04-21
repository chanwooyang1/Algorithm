from collections import deque

def bfs(x, y, team):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == team:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

M, N = map(int, input().split())  
graph = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

W_total = 0
B_total = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result = bfs(i, j, graph[i][j])
            if graph[i][j] == 'W':
                W_total += result ** 2
            else:
                B_total += result ** 2

print(W_total, B_total)
    
            