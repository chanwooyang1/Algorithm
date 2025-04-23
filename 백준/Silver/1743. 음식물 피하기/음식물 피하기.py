from collections import deque

def bfs(y, x):
	queue = deque()
	queue.append((y,x))
	visited[y][x] = True
	count = 1
	while queue:
		cy, cx  = queue.popleft()
		
		for dx, dy in [(-1, 0), (1,0), (0, -1), (0,1)]:
			nx, ny = cx + dx, cy + dy
			if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and not visited[ny][nx]:
				visited[ny][nx] = True
				queue.append((ny, nx))
				count += 1
				
	return count
	
N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for _ in range(K):
	r, c = map(int, input().split())
	graph[r-1][c-1] = 1
visited = [[False]*M for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            result = max(result, bfs(i, j))


print(result)
