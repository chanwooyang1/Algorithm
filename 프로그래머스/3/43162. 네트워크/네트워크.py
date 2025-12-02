def solution(n, computers):
    answer = 0
    nodes = [False] * n
    
    def dfs(node):
        nodes[node] = True
        for index, value in enumerate(computers[node]):
            if not nodes[index] and value == 1:
                dfs(index)
        return
    for i in range(n):
        if not nodes[i]:
            dfs(i)
            answer += 1
    return answer