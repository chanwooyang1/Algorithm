def solution(a, d, included):
    return sum([a * value + d * idx * value for idx, value in enumerate(included)])