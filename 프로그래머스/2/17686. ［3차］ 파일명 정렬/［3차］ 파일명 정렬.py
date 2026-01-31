def file_checker(text):
    num_index = 0
    for i,v in enumerate(text):
        if v.isdigit():
            num_index = i
            break
    head = text[:num_index]
    num = text[num_index:num_index+5]
    for i, v in enumerate(num):
        if not v.isdigit():
            num = num[:i]
    return(head.lower(), int(num))
    

def solution(files):
    answer = []
    files.sort(key=file_checker)
    return files