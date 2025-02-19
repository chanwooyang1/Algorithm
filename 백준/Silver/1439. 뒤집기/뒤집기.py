import sys
input = sys.stdin.readline
a = list(input().strip())
count = 0

for i in range(len(a) - 1):
    current = a[i]
    next_value = a[i + 1]
    
    if current != next_value:
        count += 1
print((count+1) // 2)    