start, end = map(int, input().split())

graph= []
for i in range(1,1001):
    for j in range(i):
        graph.append(i)

print(sum(graph[start-1:end]))