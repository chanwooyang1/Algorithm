import sys
input = sys.stdin.readline

n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

sorted_data = sorted(dots, key= lambda x: (x[1], x[0]))

for dot in sorted_data:
    print(*dot)