order = input()
total = 0
left = 0
flag = False
for ch in order:
    if ch == "(":
        left += 1
        flag = True
    else:
        if flag:
            left -= 1
            total += left
            flag = False
        else:
            left -= 1
            total += 1
        
print(str(total))