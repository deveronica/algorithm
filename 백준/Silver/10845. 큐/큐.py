#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10845                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10845                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 21:24:18 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys


N = int(input())

ans = []
for _ in range(N):
    cmd = sys.stdin.readline().split()
    e = cmd[0]

    if e == "push":
        ans.append(cmd[1])
    elif e == "pop":
        print(ans.pop(0) if ans else -1)
    elif e == "size":
        print(len(ans))
    elif e == "empty":
        print(0 if ans else 1)
    elif e == "front":
        print(ans[0] if ans else -1)
    elif e == "back":
        print(ans[-1] if ans else -1)
