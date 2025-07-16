from collections import deque
def minimum(n):
    sorted_list = sorted(n, reverse=True)
    d = deque()
    d.append(sorted_list[0])
    for i in range(1, len(sorted_list)):
        if i % 2 != 0:
            d.appendleft(sorted_list[i])
        else:
            d.append(sorted_list[i])
    max_diff = 0
    for i in range(len(d)):
        diff = abs(d[i] - d[(i+1)%len(d)])  # 원형 연결 고려
        max_diff = max(max_diff, diff)
    
    return max_diff



T = int(input())
for i in range(T):
    N = int(input())
    stomps = list(map(int, input().split()))
    result = minimum(stomps)
    print(result)