def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min_value = float("INF")
        for i in range(s, e + 1):
            if arr[i] > k:
                min_value = min(min_value, arr[i])
        if min_value != float("INF"):
            answer.append(min_value)
        else:
            answer.append(-1)
    return answer