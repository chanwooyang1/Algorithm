def solution(arr):
    stk = []
    idx = 0
    while idx < len(arr):
        if not stk:
            stk.append(arr[idx])
            idx += 1
        else:
            if stk[-1] < arr[idx]:
                stk.append(arr[idx])
                idx += 1
            else:
                stk.pop()
    return stk