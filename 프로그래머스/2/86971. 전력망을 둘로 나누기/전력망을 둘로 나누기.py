def solution(n, wires):
    answer = n
    adj = [[] for _ in range(n + 1)]
    
    for v1, v2 in wires:
        adj[v1].append(v2)
        adj[v2].append(v1)
        
    for v1, v2 in wires:
        adj[v1].remove(v2)
        adj[v2].remove(v1)
        
        visited = [False] * (n+1)
        size = dfs(v1, visited, adj)
        diff = abs(size - (n - size))
        answer = min(diff, answer)
        
        adj[v1].append(v2)
        adj[v2].append(v1)
    
   
    
    return answer

def dfs(node, visited, adj):
    count = 0
    visited[node] = True
    count += 1
    for next_node in adj[node]:
        if not visited[next_node]:
            count += dfs(next_node, visited, adj)
    return count