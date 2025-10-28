n = int(input())
p = int(input())
adj_list = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (n+1)
def dfs(node,visited):
    visited[node] = True
    
    for i in adj_list[node]:
        if not visited[i]:
            dfs(i, visited)
dfs(1, visited)

print(sum(visited) - 1)