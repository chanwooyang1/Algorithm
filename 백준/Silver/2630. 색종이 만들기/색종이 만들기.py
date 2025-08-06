#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2630                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2630                           #+#        #+#      #+#     #
#    Solved: 2025/08/06 15:15:02 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
def check(paper, size, x, y):
    val = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y + size):
            if paper[i][j] != val:
                return False
    
    return True

def quadzip(paper, size, x, y):
    global blue
    global white
    if size == 1:
        if paper[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    
    if check(paper, size, x, y):
        if paper[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    
    size = size //2

    quadzip(paper, size, x, y + size)
    quadzip(paper, size, x + size, y)
    quadzip(paper, size, x, y)
    quadzip(paper, size, x + size, y + size)


quadzip(paper, N, 0, 0)
print(str(white))
print(str(blue))
