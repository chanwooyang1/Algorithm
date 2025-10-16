def solution(brown, yellow):
    answer = []
    total = brown + yellow
    candidates = []
    for i in range(3, total + 1):
        if total % i == 0:
            candidates.append(i)
  
    for cand1 in candidates:
        for cand2 in candidates:
            if (2 * cand1) + (2 * cand2) - 4 == brown and cand1 * cand2 == total:
                if cand1 >= cand2:
                    return [cand1, cand2]
                elif cand2 >= cand1:
                    return [cand2, cand1]
    
    ## 2 x 가로 + 2 x 세로 - 4 = brown 
   