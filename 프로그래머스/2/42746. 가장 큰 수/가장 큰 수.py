def solution(numbers):
    if sum(numbers) < 1:
        return "0"
    str_numbers = [str(n) for n in numbers]
    
    str_numbers.sort(key = lambda x: x*3)
    
    return "".join(str_numbers[::-1])