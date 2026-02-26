from collections import defaultdict

def solution(clothes):
    
    clothes_dict = defaultdict(list)
    
    for name, category in clothes:
        clothes_dict[category].append(name)
    answer = 1
    print(clothes_dict)
    for key, value in clothes_dict.items():
        count = len(value) + 1
        answer *= count
    return answer - 1
    
