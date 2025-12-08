from itertools import repeat
def solution(arr, flag):
    answer = []
    for a,f in zip(arr, flag):
        if f:
            answer.extend(repeat(a, a*2))
        else:
            del answer[-a:]
    return answer