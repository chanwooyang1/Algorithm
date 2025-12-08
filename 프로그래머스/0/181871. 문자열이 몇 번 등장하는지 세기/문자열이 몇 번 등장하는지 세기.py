def solution(myString, pat):
    answer = 0
    l = len(myString)
    
    for i in range(l):
        if myString[i:].startswith(pat):
            answer += 1
    return answer