N = int(input())

result = 2
for i in range(N):
    result += (result - 1)
print(result ** 2)