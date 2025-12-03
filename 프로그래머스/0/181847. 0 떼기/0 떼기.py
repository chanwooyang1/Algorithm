def solution(n_str):
    answer = ''
    index = 0
    for char in n_str:
        if char == "0":
            continue
        else:
            index = n_str.index(char)
            break
    answer = n_str[index:]
    return answer