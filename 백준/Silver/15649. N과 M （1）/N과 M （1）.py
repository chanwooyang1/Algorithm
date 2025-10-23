N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
visited = [False] * (N+1)
def sequence(numbers, visited, M, answer):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for number in numbers:
        if not visited[number]:
            answer.append(number)
            visited[number] = True
            sequence(numbers, visited, M, answer)
            answer.pop()
            visited[number] = False
sequence(numbers, visited, M, [])    
    
    
    
    