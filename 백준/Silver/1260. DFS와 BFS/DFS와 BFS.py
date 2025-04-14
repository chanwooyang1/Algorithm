import sys
from collections import deque

input=sys.stdin.readline

n,m,start=map(int,input().split())
checked=[False]*(n+1)

graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(start):
    print(start,end=' ')
    checked[start]=True
    for i in graph[start]:
        if not checked[i]:
            dfs(i)
            

def bfs(start):
    q=deque([start])
    checked[start]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not checked[i]:
                q.append(i)
                checked[i] = True
dfs(start)
checked=[False]*(n+1)
print()
bfs(start)

    
    
