def VPS(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return "NO"
            else: 
                stack.pop()
        # print(stack)
    if stack: return "NO"
    else: return "YES"
N = int(input())
for _ in range(N):
    print(VPS(input().strip()))