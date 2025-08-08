#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4307                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4307                           #+#        #+#      #+#     #
#    Solved: 2025/08/08 16:12:15 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys


def solve():    
    l, n = map(int, sys.stdin.readline().split())
    ants = [int(sys.stdin.readline()) for _ in range(n)] 
   
    max_time = 0
    min_time = 0
    for ant in ants:
        to_left = ant
        to_right = l - ant

        min_time = max(min_time, min(to_left, to_right))
        max_time = max(max_time, max(to_left, to_right))

    print(min_time, max_time)


T = int(sys.stdin.readline())

for _ in range(T):
    solve()
    


