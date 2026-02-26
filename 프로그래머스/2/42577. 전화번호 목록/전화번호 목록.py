def solution(phone_book):
    answer = True
    min_len = float('inf')
    number_map = {}
    for number in phone_book:
        number_map[number] = True
        min_len = min(min_len, len(number))
        
    for number in phone_book:
        l = len(number)
        for i in range(min_len, l):
            if number_map.get(number[:i]):
                return False
    return True



##다른방법

