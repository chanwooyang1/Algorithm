import sys
import heapq

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = float('inf')
round = 1

while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = graph[0][0]

    pq = [(graph[0][0] , 0, 0)]
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        if x == N-1 and y == N-1:
            print(f"Problem {round}: {cost}")
            break
        if cost > dist[x][y]:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + graph[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    round += 1


