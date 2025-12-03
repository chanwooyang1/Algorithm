def solution(number):
    number_list = map(int,number)
    answer = sum(number_list) % 9
    return answer