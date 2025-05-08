N = int(input())
card_nums = set(map(int, input().split()))  
M = int(input())
integers = list(map(int, input().split()))

result = []
for i in integers:
    if i in card_nums:
        result.append("1")
    else:
        result.append("0")

print(" ".join(result))
