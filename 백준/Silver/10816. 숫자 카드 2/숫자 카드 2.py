#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10816                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10816                          #+#        #+#      #+#     #
#    Solved: 2025/01/31 20:58:59 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

dic = {}
for i in input().split():
    dic[i] = dic.get(i, 0) + 1

M = int(input())

for j in input().split():
    print(dic.get(j, 0), end=" ")
