import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dict = {}

for num in a:
    dict[num] = dict.setdefault(num, 0) + 1
for num in b:
    print(dict.setdefault(num, 0), end = " ")