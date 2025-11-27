def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i != 0:
            num = answer.pop()
            if arr[i] == num:
                answer.append(num)
                continue
            else:
                answer.append(num)
                answer.append(arr[i])
        else:
            answer.append(arr[i])
    return answer