from itertools import permutations
def solution(k, dungeons):
    max_count = 0
    
    for order in permutations(dungeons):
        stamina = k
        count = 0
        for min_req, consume in order:
            if stamina >= min_req:
                stamina -= consume
                count += 1
        max_count = max(max_count, count)
    return max_count
    
    
    
    return answer