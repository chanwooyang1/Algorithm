def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(node, visited):
        visited[node] = True
        for index, connection in enumerate(computers[node]):
            if connection == 1 and not visited[index]:
                dfs(index, visited)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, visited)
    return answer