#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11758                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11758                          #+#        #+#      #+#     #
#    Solved: 2025/08/27 09:54:42 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def check(x1, y1, x2, y2, x3, y3):
    cross = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    return  1 if cross > 0 else (-1 if cross < 0 else 0)

x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

print(check(x1,y1,x2,y2,x3,y3))