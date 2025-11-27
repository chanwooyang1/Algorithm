import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    answer = 0
    n = len(numbers) # 길이를 미리 저장
    
    # 함수 안에 함수를 만들면 외부 변수(numbers, target)를 그냥 쓸 수 있음
    def dfs(idx, current_sum):
        nonlocal answer # solution의 answer 변수를 갖다 쓰겠다는 뜻
        
        # 1. 탈출 조건: 끝까지 다 탐색했을 때
        if idx == n:
            if current_sum == target:
                answer += 1
            return # 여기서만 리턴해야 함!
        
        # 2. 수행 동작: 더하거나 빼거나 (재귀)
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])

    # DFS 시작 (인덱스 0, 합계 0)
    dfs(0, 0)
    
    return answer