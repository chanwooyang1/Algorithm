#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1446                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1446                           #+#        #+#      #+#     #
#    Solved: 2025/08/06 16:30:06 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq
N, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
for _ in range(N):
    u,v,w = map(int, input().split())
    if v > d:
        continue
    graph[u].append((v,w))

for i in range(d):
    graph[i].append((i + 1, 1))

INF = float('inf')

def dijkstra(start):
    distance = [INF] * (d+1)
    q= []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            next_node = i[0]
            weight = i[1]

            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance
shortest_paths = dijkstra(0)
print(shortest_paths[d])
