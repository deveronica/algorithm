#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11723                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11723                          #+#        #+#      #+#     #
#    Solved: 2025/02/01 18:21:20 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

M = int(sys.stdin.readline())

S = set()

for _ in range(M):
    e = sys.stdin.readline().split()
    cmd = e[0]
    try:
        x = int(e[1])
        if cmd == "check":
            print(1 if x in S else 0)
        elif cmd == "add":
            S.add(x)
        elif cmd == "remove":
            S.discard(x)
        elif cmd == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)
    except:
        if cmd == "all":
            S = set(range(1, 21))
        elif cmd == "empty":
            S.clear()
