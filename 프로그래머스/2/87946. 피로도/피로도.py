answer = 0

def dfs(stamina, count,n,visited, dungeons):
    global answer
    answer = max(answer, count)
    for i in range(n):
        if not visited[i] and stamina >= dungeons[i][0]:
            visited[i] = True
            dfs(stamina - dungeons[i][1], count + 1, n, visited, dungeons)
            visited[i] = False  # 백트래킹

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    # global answer
    # answer = 0
    dfs(k, 0,n,visited, dungeons)
    return answer
