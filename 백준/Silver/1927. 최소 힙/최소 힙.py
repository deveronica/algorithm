#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1927                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1927                           #+#        #+#      #+#     #
#    Solved: 2025/02/10 18:50:26 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    x = int(input())
    if x > 0:
        n = 0
        m = len(arr)
        if m == 0:
            arr.append(x)
        else:
            while n < m:
                if arr[(n+m) // 2] < x:
                    n = (n+m) // 2 + 1
                elif arr[(n+m) // 2] == x:
                    break
                else:
                    m = (n+m) // 2
            arr.insert((n+m) // 2, x)
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(arr[0])
            del arr[0]
