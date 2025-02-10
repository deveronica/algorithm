#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11659                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11659                          #+#        #+#      #+#     #
#    Solved: 2025/02/10 16:46:20 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n = list(map(int, input().split()))

_n = [0]
c = 0
for i in range(N):
    c += n[i]
    _n.append(c)

for _ in range(M):
    a, b = map(int, input().split())
    print(_n[b] - _n[a-1])
