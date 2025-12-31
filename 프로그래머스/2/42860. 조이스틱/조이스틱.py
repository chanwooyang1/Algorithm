def solution(name):
    n = len(name)
    answer = 0
    
    
    for char in name:
        
        diff = ord(char) - ord('A')
        answer += min(diff, 26 - diff)

   
    min_move = n - 1 
    
    for i in range(n):
        
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        distance = i + (n - next_i) + min(i, n - next_i)
        min_move = min(min_move, distance)

    answer += min_move
    return answer