
def solution(myStr):
    rp = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    answer = rp.split()
    return answer if answer else ["EMPTY"]