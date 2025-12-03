def solution(a, b):
    apb = str(a) + str(b)
    bpa = str(b) + str(a)
    return int(apb) if int(apb) >= int(bpa) else int(bpa)