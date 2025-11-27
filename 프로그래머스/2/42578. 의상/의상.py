from collections import Counter

def solution(clothes):
    # 각 종류별(kind) 개수를 자동으로 세줌
    counter = Counter([kind for name, kind in clothes])
    
    answer = 1
    for count in counter.values():
        answer *= (count + 1)
        
    return answer - 1