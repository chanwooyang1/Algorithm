def solution(n):
    answer = 0
    # graph = [[False] * n for _ in range(n)]  # 사실 안 써도 됨
    cols = [False] * n          # 열 체크
    diag1 = [False] * (2*n-1)   # 좌상-우하 대각선
    diag2 = [False] * (2*n-1)   # 우상-좌하 대각선

    def dfs(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            if not cols[col] and not diag1[row-col+n-1] and not diag2[row+col]:
                cols[col] = diag1[row-col+n-1] = diag2[row+col] = True
                dfs(row+1)
                cols[col] = diag1[row-col+n-1] = diag2[row+col] = False  # 백트래킹

    dfs(0)
    return answer
