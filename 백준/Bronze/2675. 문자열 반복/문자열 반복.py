#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2675                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2675                           #+#        #+#      #+#     #
#    Solved: 2025/01/23 18:17:24 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
T = int(input())

for _ in range(T):
    R, S = input().split()
    ans = []
    for s in list(S):
        a = int(R) * s
        ans.append(a)
    print("".join(ans))