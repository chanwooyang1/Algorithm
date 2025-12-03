def solution(arr):
    answer = 1
    l = len(arr)
    
    for i in range(l):
        for j in range(l):
            if arr[i][j] != arr[j][i]:
                answer = 0
                break
    
    return answer