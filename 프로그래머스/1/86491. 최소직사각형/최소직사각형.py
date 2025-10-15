def solution(sizes):
    left = 0
    right = 0
    for size in sizes:
        size.sort()
        if size[0] > left:
            left = size[0]
        if size[1] > right:
            right = size[1]
    
    return left * right