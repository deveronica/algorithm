#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9095                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9095                           #+#        #+#      #+#     #
#    Solved: 2025/02/10 16:29:19 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
T = int(input())

def factorial(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k

for _ in range(T):
    n = int(input())
    a1 = n
    a2 = n // 2
    a3 = n // 3

    ans = []
    for i in range(a1 + 1):
        for j in range(a2 + 1):
            for k in range(a3 + 1):
                if i + 2*j + 3*k == n:
                    x = factorial(i + j + k) / (factorial(i) * factorial(j) * factorial(k))
                    ans.append(x)
    print(int(sum(ans)))
