def solution(numLog):
    answer = []
    for i in range(1, len(numLog)):
        temp = numLog[i] - numLog[i-1]
        if temp == 1:
            answer.append("w")
        elif temp == -1:
            answer.append("s")
        elif temp == 10:
            answer.append("d")
        else:
            answer.append("a")
    return "".join(answer)