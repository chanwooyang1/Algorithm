def solution(str_list):
    answer = "".join(str_list)
    l = answer.find("l")
    r = answer.find("r")
    
    if 0 <= l < r and r != -1:
        return list(answer[:l])
    elif 0 <= r < l and l != -1:
        return list(answer[r+1:])
    elif r < 0 <= l:
        return list(answer[:l])
    elif l <0 <= r:
        return list(answer[r+1:])
    elif l < 0 and r < 0:
        return []
        