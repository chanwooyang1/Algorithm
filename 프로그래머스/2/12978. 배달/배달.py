import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    for f,t,d in road:
        graph[f].append((t, d))
        graph[t].append((f,d))
    
    distances = [float('inf')] * (N+1)
    distances[1] = 0
    
    queue = []
    heapq.heappush(queue, (0, 1))
    
    while queue:
        cd, cp = heapq.heappop(queue)
        if distances[cp] < cd:
            continue
        
        for n, d in graph[cp]:
            distance = d + cd
            if distance < distances[n]:
                distances[n] = distance
                heapq.heappush(queue, (distance, n))
    
    count = 0
    for d in distances:
        if d <= K:
            count += 1
    return count
        
    
