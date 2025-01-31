#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2751                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2751                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 17:10:15 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

print(*sorted(nums), sep="\n")
