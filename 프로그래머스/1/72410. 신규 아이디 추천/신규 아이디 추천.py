def solution(new_id):
    answer = ''
    step_one = new_id.lower()
    poss = ["a","b","c","d","e","f","g","h","i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0","1","2","3","4","5","6","7","8","9","-","_","."]
    step_two = [ c for c in step_one if c in poss] 
    
    dot_flag = False
    step_three = []
    for n in step_two:
        if n == "." and not dot_flag:
            step_three.append(n)
            dot_flag = True
        elif n == "." and dot_flag:
            continue
        else:
            step_three.append(n)
            dot_flag = False
   
    step_four = "".join(step_three).strip(".")
    step_five = []
    if not step_four:
        step_five.append("a")
    else:
        step_five = list(step_four)
    step_six = []
    if len(step_five) >= 16:
        step_six = step_five[:15]
        if step_six[-1] == ".":
            step_six = step_six[:-1]
    else:
        step_six = step_five

    if len(step_six) <= 2:
        while len(step_six) < 3:
            step_six.append(step_six[-1])
        answer = "".join(step_six)
    else:
        answer = "".join(step_six)
    return answer