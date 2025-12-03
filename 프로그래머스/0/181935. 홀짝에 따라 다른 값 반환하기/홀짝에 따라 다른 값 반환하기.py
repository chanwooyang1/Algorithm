def solution(n):
    
    return sum([x for x in range(n+1) if x % 2 != 0]) if n % 2 != 0 else sum([x**2 for x in range(n+1) if x %2 ==0])