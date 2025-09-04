import math
import sys

input = sys.stdin.readline

def calculate_area(points, theta):
    area = 0
    n = len(points)
    for i in range(n):
        area += 0.5 * points[i] * points[(i+1) % n] * math.sin(theta)
    return area

n = int(input())
scores = list(map(int, input().split()))
scores.sort(reverse=True)

theta = 2 * math.pi / n
max_area = 0

# 두 가지 지그재그 시도
for start_left in (False, True):
    zigzag = [0]*n
    left, right = 0, n-1
    for i, val in enumerate(scores):
        if (i % 2 == 0) == start_left:
            zigzag[left] = val
            left += 1
        else:
            zigzag[right] = val
            right -= 1
    area = calculate_area(zigzag, theta)
    max_area = max(max_area, area)

print(f"{max_area:.3f}")
