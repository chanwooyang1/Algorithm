import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]  
    visited = {}

    while heap:
        cost, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited[node] = cost

        if node == end:
            break

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))

    return visited.get(end, float('inf'))  

N = int(input())
M = int(input())
fee = 100001
edges= [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())

graph = {}
for frm, to, weight in edges:
    if frm not in graph:
        graph[frm] = []
    graph[frm].append((to, weight))

min_cost = dijkstra(graph, start, end)
print(min_cost)
