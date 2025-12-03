def solution(n):
    answer = [[] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer