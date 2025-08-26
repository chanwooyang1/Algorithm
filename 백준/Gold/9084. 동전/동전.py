#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9084                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: moomsss <boj.kr/u/moomsss>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9084                           #+#        #+#      #+#     #
#    Solved: 2025/08/26 15:41:35 by moomsss       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline


def count_possibilty(coins, price):
    
    dp = [0] * (price + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, price + 1):
            dp[j] += dp[j - coin]
    return dp[price]


T = int(input())
for _ in range(T):
    
    N = int(input())
    coins = list(map(int, input().split()))
    price = int(input())
    print(int(count_possibilty(coins, price)))
        