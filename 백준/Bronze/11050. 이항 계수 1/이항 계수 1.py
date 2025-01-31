#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11050                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11050                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:42:48 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, K = map(int, input().split())

ans = 1
for i in range(N, N-K, -1):
    ans *= i

for j in range(1, K+1):
    ans /= j

print(int(ans))