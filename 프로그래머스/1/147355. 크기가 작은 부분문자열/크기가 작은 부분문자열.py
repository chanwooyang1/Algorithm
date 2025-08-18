def solution(t, p):
    answer = 0
    l = len(p)
    
    for i in range(len(t) - l + 1):
        temp = ""
        for j in range(i, i + l):
            temp = temp + t[j]
        if int(temp) <= int(p):
            answer += 1
    
    return answer