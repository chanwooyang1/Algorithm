def solution(brown, yellow):
    total = brown + yellow
    for width in range(3, int(total**0.5) + 1):
        if total % width == 0:
            height = total // width
            if 2 * (width + height) - 4 == brown:
                return [height, width]  # width ≥ height로 반환
