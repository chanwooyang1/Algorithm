def solution(myString):
    answer = ''
    for char in myString:
        answer = answer + max(char, "l")
    return answer