def solution(arr):
    for i in range(0,11):
        if len(arr) == 2**i:
            return arr
        elif len(arr) < 2**i:
            l = 2**i - len(arr)
            for j in range(l):
                arr.append(0)
            return arr
        else:
            continue
    return arr