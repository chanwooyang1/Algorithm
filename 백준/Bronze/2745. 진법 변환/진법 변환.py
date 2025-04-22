N, B = input().split()
B = int(B)

result = 0
length = len(N)

for i in range(length):
    char = N[i]
    if char.isdigit():
        value = int(char)
    else:
        value = ord(char) - ord('A') + 10
    result += value * (B ** (length - i - 1))

print(result)

