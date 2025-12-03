def solution(num_list):
    answer = 0
    sumv = 0
    multiply = 1
    for num in num_list:
        sumv += num
        multiply *= num
        
    
    return 1 if multiply < sumv**2 else 0