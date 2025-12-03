def solution(my_string, m, c):
    graph = []
    for i in range(len(my_string)//m):
        graph.append(my_string[i*m : (i*m)+m])
    print(graph)
    answer = []
    for g in graph:
        answer.append(g[c-1])
    return "".join(answer)