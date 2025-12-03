def solution(todo_list, finished):
    answer = [todo for todo, result in zip(todo_list, finished) if result == False]
    return answer