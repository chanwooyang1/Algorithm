stick = input().strip()  # ✅ 입력값 받기 (strip()으로 공백 제거)
stack = []
count = 0

for i, char in enumerate(stick):
    if char == '(':
        stack.append('(')  # ✅ 열린 괄호는 스택에 추가
    else:  # ✅ 닫는 괄호일 때
        stack.pop()  # ✅ 스택에서 열린 괄호 제거

        # ✅ 레이저일 경우 (즉, 직전 문자가 '('이면)
        if stick[i - 1] == '(':
            count += len(stack)  # ✅ 레이저가 스택에 있는 모든 쇠막대기를 절단
        else:
            count += 1  # ✅ 쇠막대기의 끝이면 조각 1개 추가

print(count)  # ✅ 최종 조각 개수 출력
