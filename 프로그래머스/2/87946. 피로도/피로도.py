def solution(k, dungeons):
    answer = -1
    l = len(dungeons)
    visited = [False] * l
    
    def dfs(k, count):
        nonlocal answer
        
        if count > answer:
            answer = count
            
        for i in range(l):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1)
                visited[i] = False
    dfs(k,0 )      
    
    return answer