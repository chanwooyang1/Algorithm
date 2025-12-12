def solution(my_string, queries):
    answer = list(my_string)
    for s,e in queries:
        if s != 0:
            answer[s:e+1] = answer[e:s-1:-1]
        else:
            answer[s:e+1] = answer[e::-1]
        
    return "".join(answer)