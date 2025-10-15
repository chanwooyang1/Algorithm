def solution(answers):
    result = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    one_result = 0
    two_result = 0
    three_result = 0
    for i in range(len(answers)):
        answer = answers[i]
        i_one = i % len(one)
        i_two = i % len(two)
        i_three = i % len(three)
        
        if answer == one[i_one]:
            one_result += 1
        if answer == two[i_two]:
            two_result += 1
        if answer == three[i_three]:
            three_result += 1
    
    
    high_score = max(one_result, two_result, three_result)
    if one_result == high_score:
        result.append(1)
    if two_result == high_score:
        result.append(2)
    if three_result == high_score:
        result.append(3)
    
    
    
    return result