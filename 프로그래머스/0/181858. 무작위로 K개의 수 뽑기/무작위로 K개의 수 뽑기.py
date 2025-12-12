def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
            if len(answer) == k:
                break
    if len(answer) < k:
        answer.extend([-1] *(k - len(answer)))
    return answer