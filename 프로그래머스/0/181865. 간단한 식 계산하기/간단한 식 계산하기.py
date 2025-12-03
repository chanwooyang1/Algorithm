def solution(binomial):
    decimeters = ["+", "-","*"]
    answer = 0
    for d in decimeters:
        if d in binomial:
            a, b = map(int, binomial.split(d))
            if d == "+":
                answer = a + b
            elif d == "-":
                answer = a-b
            else:
                answer = a*b
    
    return answer