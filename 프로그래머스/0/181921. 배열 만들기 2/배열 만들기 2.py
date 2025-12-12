def solution(l, r):
    answer = []
    s = {"0","5"}
    for i in range(l, r+1):
        if not set(str(i)) - s:
            answer.append(i)
    return answer if answer else [-1]