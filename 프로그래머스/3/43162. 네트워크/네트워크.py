def solution(n, computers):
    answer = 0
    ## 0번부터 n-1 까지 돌면서 하나 들어가서 네트워크 1늘리고 꼬리물고물고 dfs로 다 탐색하고 나와서 방문안한 노드가 나오면 네트워크 개수 1늘리고 다시 또 반복
    
    def dfs(node, computers, visited):
        visited[node] = True
        computer = computers[node]
        for i in range(len(computer)):
            if computer[i] == 1 and not visited[i]:
                dfs(i, computers, visited)
                
        
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers, visited)
            
    return answer