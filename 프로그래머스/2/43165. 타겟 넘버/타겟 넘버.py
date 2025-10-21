def solution(numbers, target):
    answer = 0
     
    def dfs(index, current):
        nonlocal answer
        
        if index == (len(numbers)):
            if  current == target:
                answer += 1
                return 
            return
        dfs(index + 1, current + numbers[index])
        dfs(index + 1, current - numbers[index])
        
        
    dfs(0 , 0)        
    return answer