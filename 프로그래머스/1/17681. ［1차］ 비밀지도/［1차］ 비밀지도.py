def solution(n, arr1, arr2):
    answer = []
    bi_arr1 = []
    bi_arr2 = []
    for num in arr1:
        bi_num = bin(num)[2:]
        bi_arr1.append(bi_num.rjust(n,'0'))
    for num in arr2:
        bi_num = bin(num)[2:]
        bi_arr2.append(bi_num.rjust(n,'0'))
    print(bi_arr1)
    print(bi_arr2)
    for i in range(n):
        line = ""
        for j in range(n):
            suffix = " " if bi_arr1[i][j] == bi_arr2[i][j] and bi_arr1[i][j] == "0" else "#"
            line += suffix
        answer.append(line)
    print(answer)
            
                
    
    
    return answer