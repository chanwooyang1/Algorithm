def solution(code):
    answer = []
    mode = 0
    
    for i,c in enumerate(code):
        if mode == 0:
            if c == "1":
                mode = 1
            else:
                if i % 2 == 0:
                    answer.append(c)
        else:
            if c == "1":
                    mode = 0
            else:
                if i % 2 != 0:
                    answer.append(c)
    return "".join(answer) if answer else "EMPTY"