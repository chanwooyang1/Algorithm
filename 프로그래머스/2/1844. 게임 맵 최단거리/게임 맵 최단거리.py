from collections import deque
def solution(maps):
   
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue.append((0,0,1))
    visited[0][0] = True
    
    while queue:
        
        x, y, count = queue.popleft()
        
        
        if x == n - 1 and y == m - 1:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= n - 1 and 0 <= ny <= m-1 and not visited[nx][ny] and maps[nx][ny] == 1:
                queue.append((nx,ny, count + 1))
                visited[nx][ny] = True
    return -1
    
    