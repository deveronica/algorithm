#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2739                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2739                           #+#        #+#      #+#     #
#    Solved: 2025/01/23 17:42:50 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
for i in range(9):
    print(f"{N} * {i+1} = {N*(i+1)}")