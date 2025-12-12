def solution(picture, k):
    answer = []
    
    for p in picture:
        temp = []
        for i in p:
            temp.append(i*k)
        
        for j in range(k):
            
            answer.append("".join(temp))
        
    return answer