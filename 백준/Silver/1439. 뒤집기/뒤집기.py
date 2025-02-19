import sys
input = sys.stdin.readline  # 빠른 입력을 위해 사용

count1 = 0

# 문자열 입력받기
input_str = input().strip()  # 개행 문자 제거
length = len(input_str)

# 인접한 문자 비교
for i in range(length - 1):
    current = input_str[i]
    next_char = input_str[i + 1]
    
    if current != next_char:
        count1 += 1

# 결과 출력 (정수 나눗셈 사용)
print((count1 + 1) // 2)
