from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dt = [[1,0],[-1,0],[0,1],[0,-1]]
village = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in dt:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            village.append(bfs(i, j))

village.sort()
print(len(village))
for v in village:
    print(v)

        