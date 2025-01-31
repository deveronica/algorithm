#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1978                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1978                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 15:41:43 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

cnt = 0
for num in list(map(int, input().split())):
    if num <= 1:
        continue
    elif num == 2:
        cnt += 1
        continue
    for i in range(2, num):
        if num % i == 0:
            break
        if i == num - 1:
            cnt += 1
            break

print(cnt)
