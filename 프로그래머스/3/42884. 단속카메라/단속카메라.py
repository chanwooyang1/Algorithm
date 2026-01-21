def solution(routes):
    answer = 0
    routes.sort(key=lambda x : (x[1], x[0]))
    print(routes)
    combine = []
    for s,e in routes:
        if not combine or combine[-1][1] < s:
            combine.append([s,e])
            answer += 1
        else:
            continue
        print(combine)
    
    return len(combine)