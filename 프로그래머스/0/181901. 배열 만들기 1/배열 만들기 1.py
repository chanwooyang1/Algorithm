def solution(n, k):
    sum = 0
    answer = []
    for i in range(n):
        sum += k
        if sum > n:
            break
        answer.append(sum)
    return answer