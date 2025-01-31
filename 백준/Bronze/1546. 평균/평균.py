#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1546                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1546                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:25:33 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
scores = list(map(int, input().split()))

print(sum(scores) / len(scores) * (100 / max(scores)))