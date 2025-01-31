#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1018                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 17:55:17 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

N, M = map(int, sys.stdin.readline().split())
nums = [[1 if k == "W" else -1 for k in list(sys.stdin.readline())] for _ in range(N)]

def calc(x, y):
    ans1 = 0
    ans2 = 0
    for idx, num in enumerate(nums[x:x+8]):
        if idx % 2 == 0:
            ans1 += sum(num[y:y+8:2])
            ans2 += sum(num[y+1:y+8:2])
        elif idx % 2 != 0:
            ans1 += sum(num[y+1:y+8:2])
            ans2 += sum(num[y:y+8:2])
    case1 = abs(32 - ans1) / 2 + abs(-32 - ans2) / 2
    case2 = abs(-32 - ans1) / 2 + abs(32 - ans2) / 2
    return min(case1, case2)

a, b = N - 8, M - 8

best = 32
for i in range(a + 1):
    for j in range(b + 1):
        new = calc(i, j)
        if new < best:
            best = new

print(int(best))
