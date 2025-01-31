#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10814                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10814                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 17:42:12 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

infos = []
for idx in range(N):
    a, b = input().split()
    infos.append((int(a), b, idx))

ans = sorted(infos, key=lambda x: (x[0], x[2]))

for answer in ans:
    print(f"{answer[0]} {answer[1]}")
