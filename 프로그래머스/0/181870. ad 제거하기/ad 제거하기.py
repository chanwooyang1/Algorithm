def solution(strArr):
    answer = []
    for sa in strArr:
        if "ad" in sa:
            continue
        else:
            answer.append(sa)
    return answer