#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2609                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2609                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:31:17 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
a, b = map(int, input().split())

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
    else:
        continue

for j in range(max(a, b), a * b + 1, i):
    if j % a == 0 and j % b == 0:
        print(j)
        break
    else:
        continue
