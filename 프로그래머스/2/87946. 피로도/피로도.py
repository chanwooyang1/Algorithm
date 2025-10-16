from itertools import permutations


def solution(k, dungeons):
    answer = -1
    
    for p in permutations(dungeons):
        stamina = k
        count = 0
        for dungeon in p:
            if stamina >= dungeon[0]:
                stamina -= dungeon[1]
                count += 1
        answer = max(count, answer)
    return answer