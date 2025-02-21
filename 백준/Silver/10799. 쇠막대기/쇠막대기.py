stick = input()
stack = []
count = 0
for i in range(len(stick) - 1):
    if stick[i] == '(' and stick[i+1] == ')':
        count += len(stack)
    elif stick[i] == ')' and stick[i - 1] != '(':
        stack.pop()
        count += 1
    elif stick[i] == '(':
        stack.append('(')
if len(stack) != 0:
    count += 1
print(count)