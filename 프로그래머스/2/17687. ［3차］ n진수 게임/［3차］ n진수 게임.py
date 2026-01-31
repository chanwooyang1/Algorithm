def solution(n, t, m, p):
    answer = [] 
    num = 0
    candidate = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    
    while len(answer) < m * t:
        temp = []
    
        if num == 0:
            temp.append("0")
        else:
            temp_num = num
            while temp_num > 0:
    
                rem = temp_num % n 
                temp.append(candidate[rem]) 
                temp_num = temp_num // n 
        
        
        answer += temp[::-1]
        num += 1
        
    full_str = "".join(answer)
    
    return full_str[p-1::m][:t]