N = int(input())

for _ in range(N):
    input_str = input()
    stack = []
    is_valid = True  

    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                print("NO")
                is_valid = False 
                break  
            stack.pop()
    
    if is_valid:
        if not stack:
            print("YES")
        else:
            print("NO")
