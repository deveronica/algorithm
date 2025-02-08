#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11399                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11399                          #+#        #+#      #+#     #
#    Solved: 2025/02/09 03:10:38 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
P = list(map(int, input().split()))

P.sort(key=lambda x: x)

ans = 0
for i in range(N):
    n = N - i
    ans += P[i] * n

print(ans)
