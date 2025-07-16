N, M = map(int, input().split())
visited = [False] * (N + 1)
path = []

def dfs(s):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    for i in range(s, N + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs(i+1)
            visited[i] = False
            path.pop()
dfs(1)