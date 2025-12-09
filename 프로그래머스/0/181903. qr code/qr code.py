def solution(q, r, code):
    answer = ''
    for idx, ch in enumerate(code):
        if idx % q == r:
            answer += ch
    return answer