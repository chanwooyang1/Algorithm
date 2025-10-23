N, M = map(int, input().split())
visited = [False] * (N+1)
answer = []
def dfs(start):
    if len(answer) == M:
        print(" ".join(map(str,answer)))
        return
        
    for i in range(start, N+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            dfs(i+1)
            answer.pop()
            visited[i] = False
dfs(1)