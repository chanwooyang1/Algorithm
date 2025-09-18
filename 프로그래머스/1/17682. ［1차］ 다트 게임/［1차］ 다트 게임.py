def solution(dartResult):
    answer = [[] for _ in range(3)]
    flag = False
    num = -1
    for i in range(len(dartResult)):
        ch = dartResult[i]
        if ch == '1':
            flag = True
        if ch == '0' and flag:
            answer[num].pop()
            answer[num].append("10")
            flag = False
            continue
        if ch.isdigit():
            num += 1
        else:
            flag = False
        answer[num].append(ch)
        
    points = []    
    for i in range(3):
        point = 0
        for j in answer[i]:
            if j.isdigit():
                point = int(j)
            else:
                if j == "S":
                    continue
                elif j == "D":
                    point = pow(point, 2)
                elif j == "T":
                    point = pow(point, 3)
                elif j == "*":
                    point *= 2
                    if i > 0:
                        points[i - 1] = points[i-1] * 2
                elif j == "#":
                    point *= -1
        points.append(point)
        
    
                    
                
        
    return sum(points)