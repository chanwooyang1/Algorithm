import sys
input = sys.stdin.readline

N = int(input())
stack = []
outputs = []

for _ in range(N):
    orders = input().split()
    command = int(orders[0])

    if command == 1:
        stack.append(int(orders[1]))
    elif command == 2:
        outputs.append(str(stack.pop()) if stack else '-1')
    elif command == 3:
        outputs.append(str(len(stack)))
    elif command == 4:
        outputs.append('0' if stack else '1')
    elif command == 5:
        outputs.append(str(stack[-1]) if stack else '-1')

print('\n'.join(outputs))
