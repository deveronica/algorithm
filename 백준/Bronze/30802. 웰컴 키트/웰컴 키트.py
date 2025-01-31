#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30802                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30802                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 14:58:27 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

answer = 0
for size in sizes:
    n = size // T if size != 0 else 0
    n += 1 if size % T != 0 else 0
    answer += n

print(answer)
print(f"{N // P} {N % P}")
