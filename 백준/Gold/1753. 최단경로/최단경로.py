import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())


adj = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,w = map(int, input().split())
    adj[a].append((b,w))
    
answer = [float('inf')] * (v+1)
answer[k] = 0
pq = [(0, k)]    
while pq:
    d, node = heapq.heappop(pq)
    if d > answer[node]:
        continue
    for nxt, w in adj[node]:
        new_cost = d + w
        if new_cost < answer[nxt]:
            answer[nxt] = new_cost
            heapq.heappush(pq,(new_cost, nxt))

for i in range(1, v + 1):
    print("INF" if answer[i] == float('inf') else answer[i])  


