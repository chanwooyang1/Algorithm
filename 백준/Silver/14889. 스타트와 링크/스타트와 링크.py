from itertools import combinations
N = int(input())
answer = float('inf')
stats = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
start_team = []
link_team = []
def calculate(team1, team2):
    team_one = 0
    team_two = 0
    for a,b in combinations(team1,2):
        team_one += stats[a][b] + stats[b][a]
    for c,d in combinations(team2, 2):
        team_two += stats[c][d] + stats[d][c]
    return abs(team_one - team_two)
    

def dfs(idx):
    global answer
    if len(start_team) == N // 2:
        link_team = [i for i in range(N) if i not in start_team]
        score = calculate(start_team, link_team)
        answer = min(answer, score)
        return
    
    for j in range(idx, N):
        if not visited[j]:
            start_team.append(j)
            visited[j] = True
            dfs(j + 1)
            start_team.pop()
            visited[j] = False
dfs(0)
print(answer)