def solution(rows, columns, queries):
    answer = []
    graph = []
    numbers = list(range(1, (rows * columns) + 1))
    graph = [numbers[i : i+columns] for i in range(0, len(numbers), columns)]
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1 
        
        temp = graph[x1][y1]
        min_value = temp
        
        
        for k in range(x1, x2):
            graph[k][y1] = graph[k+1][y1]
            min_value = min(graph[k][y1], min_value)
        for k in range(y1, y2):
            graph[x2][k] = graph[x2][k+1]
            min_value = min(graph[x2][k], min_value)
        for k in range(x2, x1, -1):
            graph[k][y2] = graph[k-1][y2]
            min_value = min(graph[k][y2], min_value)
        for k in range(y2, y1, -1):
            graph[x1][k] = graph[x1][k-1]
            min_value = min(graph[x1][k], min_value)
        graph[x1][y1 + 1] = temp
        min_value = min(temp, min_value)
        answer.append(min_value)
        
    return answer