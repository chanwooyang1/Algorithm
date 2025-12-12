from collections import Counter
def solution(a, b, c, d):
    answer = 0
    nums = Counter([a,b,c,d])
    sorted_counts = nums.most_common()
    if len(nums) == 1:
        return 1111 * a
    elif len(nums) == 4:
        return min(a,b,c,d)
    elif len(nums) == 2:
        (p, count_p), (q, count_q) = sorted_counts
        
        if count_p > count_q:
            return (10 * p + q)**2
        else:
            return (p + q) * abs(p-q)
    elif len(nums) == 3:
        (p, count_p), (q, count_q), (r, count_r) = sorted_counts
        return q * r
        
    return answer