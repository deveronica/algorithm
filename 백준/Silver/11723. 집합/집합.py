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
    
    if e[0] == "add":
        if e[1] not in S:
            S.add(e[1])
    elif e[0] == "remove":
        if e[1] in S:
            S.remove(e[1])
    elif e[0] == "check":
        print(1 if e[1] in S else 0)
    elif e[0] == "toggle":
        if e[1] in S:
            S.remove(e[1])
        elif e[1] not in S:
            S.add(e[1])
    elif e[0] == "all":
        S = set(map(str, range(1, 21)))
    elif e[0] == "empty":
        S = set()