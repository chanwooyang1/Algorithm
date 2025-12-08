def solution(myString, pat):
    answer = 0
    pointer = 0
    while True:
        idx = myString.find(pat, pointer)
        if idx == -1:
            break
        answer += 1
        pointer = idx + 1
    return answer