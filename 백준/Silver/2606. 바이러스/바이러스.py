from collections import deque, defaultdict

N = int(input())
p = int(input())

graph = defaultdict(list)
for _ in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  

visited = [False] * (N + 1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    count = 0
    
    
    while q:
        current = q.popleft()
        if current != 1:
        	count += 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                
    return count

print(bfs(1))
