N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())

min_answer = float('inf')
max_answer = float('-inf')

def dfs(depth, total, plus, minus, multiple, divide):
    global min_answer, max_answer
    if depth == N:
        min_answer = min(min_answer, total)
        max_answer = max(max_answer, total)
        return

    if plus > 0:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiple, divide)
    if minus > 0:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiple, divide)
    if multiple > 0:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiple - 1, divide)
    if divide > 0:
        # 문제 조건에 맞는 나눗셈 처리
        if total < 0:
            dfs(depth + 1, -(-total // numbers[depth]), plus, minus, multiple, divide - 1)
        else:
            dfs(depth + 1, total // numbers[depth], plus, minus, multiple, divide - 1)

dfs(1, numbers[0], plus, minus, multiple, divide)

print(max_answer)
print(min_answer)
