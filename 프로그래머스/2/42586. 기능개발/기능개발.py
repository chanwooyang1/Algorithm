from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    sq = deque(speeds)
    while q:
        
        for i in range(len(q)):
            q[i] += sq[i]
        
        count = 0
        
        while q and q[0] >= 100:
            count += 1
            q.popleft()
            sq.popleft()
        
        if count >= 1:
            answer.append(count)
        
    
    return answer