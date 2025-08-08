import sys

def solve():
    l, n = map(int, sys.stdin.readline().split()) # sys.stdin.readline 사용
    
    ant_positions = []
    for _ in range(n):
        ant_positions.append(int(sys.stdin.readline())) # sys.stdin.readline 사용
    
    min_fall_time = 0
    max_fall_time = 0

    for p in ant_positions:
        time_to_left = p
        time_to_right = l - p

        # min_fall_time: 각 개미가 가장 가까운 끝으로 갈 때의 시간 중 최댓값
        min_fall_time = max(min_fall_time, min(time_to_left, time_to_right))
        
        # max_fall_time: 각 개미가 가장 먼 끝으로 갈 때의 시간 중 최댓값
        max_fall_time = max(max_fall_time, max(time_to_left, time_to_right))
        
    print(min_fall_time, max_fall_time)

T = int(sys.stdin.readline()) # sys.stdin.readline 사용
for _ in range(T):
    solve()