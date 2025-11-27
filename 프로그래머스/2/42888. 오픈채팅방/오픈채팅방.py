def solution(record):
    answer = []
    behaves = []
    ids = {}
   
    for rc in record:
        words = rc.split()
        if len(words) == 3:
            if words[0] == "Enter":
                behaves.append((words[1],words[0]))
                ids[words[1]] = words[2]
            else:
                ids[words[1]] = words[2]
        else:
            behaves.append((words[1],words[0]))
            
            
        
    for user_id, behave in behaves:
        name = ids[user_id]
        if behave == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        else:
            answer.append(f"{name}님이 나갔습니다.")
    
    return answer