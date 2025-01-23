#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10951                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10951                          #+#        #+#      #+#     #
#    Solved: 2025/01/23 17:45:47 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
try:
    while True:
        K = input()
        if not K:
            break
        else:
            A, B = map(int, K.split())
        print(A+B)
except:
    exit()
