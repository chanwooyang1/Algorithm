def solution(str_list):
    for idx, val in enumerate(str_list):
        if str_list[idx] == "l":
            return str_list[:idx]
        elif str_list[idx] == "r":
            return str_list[idx+1:]
    return []