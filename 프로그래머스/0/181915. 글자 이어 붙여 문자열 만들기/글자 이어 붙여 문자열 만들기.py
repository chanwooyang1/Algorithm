def solution(my_string, index_list):
    answer = ''
    for index in index_list:
        answer  = answer + my_string[index]
    return answer