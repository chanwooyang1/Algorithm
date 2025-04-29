from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()
result = []
for _ in range(N):
	command = list(input().split())
	if command[0] == "push":
		num = int(command[1])
		queue.append(num)
	elif command[0] == 'pop':
		if queue:
			result.append(queue.popleft())
		else:
			result.append(-1)
	elif command[0] == 'size':
		result.append(len(queue))
	elif command[0] == 'empty':
		if queue:
			result.append(0)
		else:
			result.append(1)
	elif command[0] == 'front':
		if queue:
			result.append(queue[0])
		else: result.append(-1)
	elif command[0] == 'back':
		if queue:
			result.append(queue[-1])
		else: result.append(-1)
print('\n'.join(map(str, result)))
