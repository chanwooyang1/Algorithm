def solution(ineq, eq, n, m):
    answer = 0
    condition_1 = True
    condition_2 = True
    
    
    if ineq == "<":
        condition_1 = True
    else:
        condition_1 = False
        
    if eq == "=":
        condition_2 = True
    else:
        condition_2 = False
        
    if condition_1 and condition_2:
        return int(n <= m) 
    elif condition_1 and not condition_2:
        return int(n < m)
    elif not condition_1 and condition_2:
        return int(n >= m)
    elif not condition_1 and not condition_2:
        return int(n > m)
    
    return answer