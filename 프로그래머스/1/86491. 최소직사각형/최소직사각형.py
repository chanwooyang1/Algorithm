def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        w = max(max(size), w)
        h = max(min(size), h)
    return w*h