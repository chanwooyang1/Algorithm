def check(graph, x, y, size, val):
    """모든 요소가 동일한지 확인하는 함수"""
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != val:
                return False
    return True


def recursive(graph, x, y, size):
    """재귀적으로 그래프를 탐색하는 함수"""
    if check(graph, x, y, size, graph[y][x]):
        result.append(graph[y][x])
        return
    
    result.append('(')
    half = size // 2
    recursive(graph, x, y, half)                     # 좌상단
    recursive(graph, x + half, y, half)              # 우상단
    recursive(graph, x, y + half, half)              # 좌하단
    recursive(graph, x + half, y + half, half)       # 우하단
    result.append(')')


# 메인 코드
N = int(input())
graph = [input() for _ in range(N)]  # 리스트 컴프리헨션 사용으로 더 간결하게
result = []

recursive(graph, 0, 0, len(graph))
print("".join(result))
