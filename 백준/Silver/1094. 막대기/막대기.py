#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1094                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1094                           #+#        #+#      #+#     #
#    Solved: 2025/08/08 15:13:16 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
X = int(input())
sticks = [64]

while True:
    sticks = sorted(sticks, reverse=True)
    sum_sticks = sum(sticks)
    if  sum_sticks == X:
        break
    elif sum(sticks) > X:
        shortest = sticks.pop()
        left_sum = sum(sticks) + shortest // 2
        if left_sum >= X:
            sticks.append(shortest // 2)
        else:
            sticks.append(shortest//2)
            sticks.append(shortest//2)

print(len(sticks))





