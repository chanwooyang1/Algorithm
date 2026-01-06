def solution(people, limit):
    answer = 0
    sorted_people = sorted(people)
    left, right = 0, (len(people) - 1)
    
    while left <= right:
        if sorted_people[left] + sorted_people[right] > limit:
            answer += 1
            right -= 1
        else:
            answer += 1
            right -= 1
            left += 1
    return answer
    
    return answer