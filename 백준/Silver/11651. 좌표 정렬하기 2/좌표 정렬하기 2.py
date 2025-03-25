N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = sorted(graph, key = lambda x: (x[1], x[0]))
for line in result:
    print(" ".join(map(str, line)))