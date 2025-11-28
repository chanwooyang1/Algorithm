from collections import deque
def solution(priorities, location):
    
    idx = deque(range(len(priorities)))
    p = deque(priorities)
    count = 0
    while p:
        first = p[0]
        if first >= max(p):
            count += 1
            p.popleft()
            temp = idx.popleft()
            if location == temp:
                break
        else:
            temp = p.popleft()
            p.append(temp)
            idx_temp = idx.popleft()
            idx.append(idx_temp)
        print(count)
        print(p)
        print(idx)
    return count