#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10828                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10828                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 21:03:54 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input())

ans = []
cnt = 0
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        ans.append(cmd[1])
        cnt += 1
    elif cmd[0] == "pop":
        if cnt > 0:
            print(ans.pop(-1))
            cnt -= 1
        else:
            print(-1)
    elif cmd[0] == "size":
        print(cnt)
    elif cmd[0] == "empty":
        if cnt:
            print(0)
        else:
            print(1)
    elif cmd[0] == "top":
        if cnt:
            print(ans[-1])
        else:
            print(-1)
