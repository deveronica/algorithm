#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2805                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2805                           #+#        #+#      #+#     #
#    Solved: 2025/02/11 00:26:02 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hs = list(map(int, input().split()))

hs.sort(reverse=True)

num = 0
for i in range(N):
    num += hs[i]
    if num - hs[i]*(i+1) >= M:
        bs = hs[:i]
        break
    else:
        bs = hs

length = len(bs)
mini = sum(bs[:-1]) - bs[-1] * (length - 1)
target = M - mini
ans = target // length
cond = target % length

print(bs[-1] - ans if not cond else bs[-1] - ans - 1)
