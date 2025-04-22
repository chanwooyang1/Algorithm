from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1))  # 시작 위치와 거리
    visited[y][x] = True

    while queue:
        cx, cy, count = queue.popleft()

        if cx == M - 1 and cy == N - 1:
            return count

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and graph[ny][nx] == '1':
                    visited[ny][nx] = True
                    queue.append((nx, ny, count + 1))

    return -1 


N, M = map(int, input().split())
graph = [input().strip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]


print(bfs(0, 0))
