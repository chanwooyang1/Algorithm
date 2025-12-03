def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        ms = my_strings[i]
        f = parts[i][0]
        t = parts[i][1]
        
        answer += ms[f:t+1]
        
    return answer