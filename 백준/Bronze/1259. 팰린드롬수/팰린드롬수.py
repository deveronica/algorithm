#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1259                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1259                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:21:05 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
while True:
    a = input()
    if a == "0":
        break
    b = len(a) // 2
    print("yes" if a[:b] == a[::-1][:b] else "no")
