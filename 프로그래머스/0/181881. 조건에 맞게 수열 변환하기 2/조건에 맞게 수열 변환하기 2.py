def solution(arr):
    answer = []
    answer.append(arr)
    pointer = 0
    while True:
        temp = answer[pointer].copy()
        for idx, t in enumerate(temp):
            if t >= 50 and t % 2 == 0:
                temp[idx] = t//2
            elif t < 50 and t % 2 != 0:
                temp[idx] = t*2 + 1
        
        if answer[pointer] == temp:
            return pointer
        else:
            answer.append(temp)
            pointer += 1
        
    