#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11053                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11053                          #+#        #+#      #+#     #
#    Solved: 2025/09/04 09:47:49 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = []

for num in A:
    pos = bisect.bisect_left(dp, num)

    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))
