from itertools import combinations
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
        


def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            answer += 1
    return answer


    