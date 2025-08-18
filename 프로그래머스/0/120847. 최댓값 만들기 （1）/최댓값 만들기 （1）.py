def solution(numbers):
    answer = 0
    numbers.sort()
    max1 = numbers.pop()
    max2 = numbers.pop()
    return max1 * max2