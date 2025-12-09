def solution(my_string):
    answer = [0] * 52
    for ch in my_string:
        if ch.isupper():
            answer[ord(ch) - 65] += 1
        if ch.islower():
            answer[ord(ch) - 71] += 1
    return answer