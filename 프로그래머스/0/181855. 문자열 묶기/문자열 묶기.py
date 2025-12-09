def solution(strArr):
    answer = [[] for _ in range(31)]
    for strarr in strArr:
        l = len(strarr)
        answer[l].append(strarr)
    return max(len(s) for s in answer)