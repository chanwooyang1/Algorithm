
import sys
input = sys.stdin.readline
N,M =map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

answer= 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while True:
    # 시작 자리가 청소가 되어있지 않을때
    if graph[r][c] == 0:
        graph[r][c] =2
        answer +=1

    cline = False

    # 청소되지 않은 4개의 방향을 확인
    for i in range(1,5):
        x = r + dx[(d-i)%4]
        y = c + dy[(d-i)%4]

        if 0<=x<N and 0<=y<M:
            if graph[x][y]==0:
                r,c = x,y
                graph[x][y]=2
                answer+=1
                d = (d-i)%4
                cline=True
                break

    # 4개의 방향이 청소할 곳이 없다면 후진
    if not cline:
        x = r + dx[(d - 2) % 4]
        y = c + dy[(d - 2) % 4]
        if 0<=x<N and 0<=y<M:
            r = x
            c = y
            if graph[x][y]==1:
                break
        else:
            break

print(answer)