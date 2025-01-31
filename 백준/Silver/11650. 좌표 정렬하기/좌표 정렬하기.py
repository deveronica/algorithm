#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11650                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11650                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 17:50:33 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

nums = []
for _ in range(N):
    a, b = map(int, input().split())
    nums.append((a, b))

for num in sorted(nums, key=lambda x: (x[0], x[1])):
    print(num[0], num[1], sep=" ")
