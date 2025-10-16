def solution(n, wires):
    answer = n
    adj = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    
    
    for v1, v2 in wires:
        visited = [False] * (n + 1)
        have = dfs(v1,adj, visited,  (v1,v2))
        diff = abs(have - (n - have))
        answer = min(diff, answer)
    
    
    return answer
def dfs(node,adj, visited, cut):
    visited[node] = True
    count = 1
    for next_node in adj[node]:
        if not visited[next_node] and cut != (node, next_node) and cut != (next_node, node):
            count += dfs(next_node,adj, visited, cut)
    return count
    
    