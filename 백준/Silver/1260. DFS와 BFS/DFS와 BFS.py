import sys
from collections import deque
input = sys.stdin.readline
N, M , V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

    
for i in range(1, N+1):
    adj_list[i].sort()

    
def dfs(node, visited):
    visited[node] = True
    print(node, end = " ")
    for next_node in adj_list[node]:
        if not visited[next_node]:
            dfs(next_node, visited)

            
def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False] * (N+1)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end= " ")
        for next_node in adj_list[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
dfs_visited = [False] * (N+1)
dfs(V, dfs_visited)
print()
bfs(V)
    