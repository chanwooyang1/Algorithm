N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j, board[i][j]))

min_blind = float('inf')
dirs_list = []

def watch(x, y, dir, temp):
    nx, ny = x + dx[dir], y + dy[dir]
    while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
        if temp[nx][ny] == 0:
            temp[nx][ny] = '#'
        nx += dx[dir]
        ny += dy[dir]

def dfs(depth):
    global min_blind
    if depth == len(cctvs):
        # 모든 CCTV 방향이 결정된 시점
        temp = [row[:] for row in board]
        for i, (x, y, t) in enumerate(cctvs):
            for d in dirs_list[i]:
                watch(x, y, d, temp)
        cnt = sum(row.count(0) for row in temp)
        min_blind = min(min_blind, cnt)
        return

    _, _, t = cctvs[depth]
    for dirs in directions[t]:
        dirs_list.append(dirs)
        dfs(depth + 1)
        dirs_list.pop()

dfs(0)
print(min_blind)
