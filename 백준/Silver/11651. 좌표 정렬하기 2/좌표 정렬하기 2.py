import sys
input = sys.stdin.readline
write = sys.stdout.write  # write를 간단하게 씀

n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

dots.sort(key=lambda x: (x[1], x[0]))

for x, y in dots:
    write(f"{x} {y}\n")