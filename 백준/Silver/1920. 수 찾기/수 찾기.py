#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 19:45:15 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

dic = {}
for i in input().split():
    dic[int(i)] = 1

M = int(input())

for j in input().split():
    print(dic.get(int(j), 0))
