from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        word, depth = queue.popleft()
        
        if word == target:
            return depth
        for next_word in words:
            if next_word not in visited and is_one_diff(word, next_word):
                visited.add(word)
                queue.append((next_word, depth+1))
    
    
    return 0
def is_one_diff(a, b):
    """두 단어가 정확히 한 글자만 다르면 True"""
    diff_count = sum(1 for x, y in zip(a, b) if x != y)
    return diff_count == 1