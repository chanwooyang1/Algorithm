def solution(arr):
    
    r = len(arr)
    c = len(arr[0])
    if r > c:
        for i in range(r):
            arr[i].extend([0] * (r-c))
    elif c > r:
        for _ in range(c - r):
            arr.append([0] * c)
    return arr