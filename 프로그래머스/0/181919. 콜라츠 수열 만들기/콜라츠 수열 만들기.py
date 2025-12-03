def solution(n):
    answer = []
    answer.append(n)
    while True:
        num = answer[-1]
        if num == 1:
            break
        if num % 2 == 0:
            answer.append(num // 2)
        else:
            answer.append(num * 3  + 1)
    return answer