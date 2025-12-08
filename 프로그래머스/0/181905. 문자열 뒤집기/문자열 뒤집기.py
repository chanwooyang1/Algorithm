def solution(my_string, s, e):
    
    ml = list(my_string)
    ml[s:e+1] = ml[s:e+1][::-1]
    return "".join(ml)