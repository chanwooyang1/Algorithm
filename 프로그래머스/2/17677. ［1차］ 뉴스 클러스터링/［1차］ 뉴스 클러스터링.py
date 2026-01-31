from collections import Counter
def solution(str1, str2):
    answer = 0
    s_str1 = []
    s_str2 = []
    
    for i, v in enumerate(str1):
        if i <= len(str1) - 2:
            temp = str1[i:i+2].lower()
            if temp.isalpha():
                
                s_str1.append(temp)
            else: continue
    for i, v in enumerate(str2):
        if i <= len(str2) - 2:
            temp = str2[i:i+2].lower()
            if temp.isalpha():
                
                s_str2.append(temp)
            else: continue

    if not s_str1 and not s_str2 :
        return 65536
    
    c1 = Counter(s_str1)
    c2 = Counter(s_str2)
    
    answer = sum((c1 & c2).values()) / sum((c1 | c2).values())
    answer = answer * 65536
    
    return int(answer)