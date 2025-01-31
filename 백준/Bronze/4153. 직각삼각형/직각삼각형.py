#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4153                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4153                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 11:51:45 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if max(a, b, c) > c:
        if a > b:
            a, c = c, a
        elif a < b:
            c, b = b, c
        elif a == b:
            print("wrong")
            continue
    print("right" if a ** 2 + b ** 2 == c ** 2 else "wrong")