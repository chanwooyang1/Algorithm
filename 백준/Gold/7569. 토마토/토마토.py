from collections import deque

M, N, H = map(int, input().split())
boxes = []
for i in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    boxes.append(layer)
dz = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]

queue = deque()

for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y] == 1:
                queue.append((z,x,y))
                
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz, nx, ny = z + dz[i], x +dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if boxes[nz][nx][ny] == 0:
                boxes[nz][nx][ny] = boxes[z][x][y] + 1  
                queue.append((nz,nx,ny))
days = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y] == 0:      # 익지 않은 토마토 존재
                print(-1)
                exit(0)
            days = max(days, boxes[z][x][y])

print(days - 1)