def solution(arr, queries):
    for s, e in queries:
        for i in range(len(arr)):
            if s<= i <= e:
                arr[i] =  arr[i] + 1
    return arr