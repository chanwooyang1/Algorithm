t = int(input())
for _ in range(t):
    elements = list(map(int, input().split()))
    elements.sort()
    print(elements[-3])