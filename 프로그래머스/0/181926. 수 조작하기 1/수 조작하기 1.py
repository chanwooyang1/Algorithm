def solution(n, control):
    answer = n
    for char in control:
        if char == "w":
            answer += 1
        elif char == "s":
            answer -= 1
        elif char == "d":
            answer += 10
        else:
            answer -= 10
    return answer