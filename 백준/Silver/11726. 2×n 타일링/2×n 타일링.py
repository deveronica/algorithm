#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11726                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11726                          #+#        #+#      #+#     #
#    Solved: 2025/02/10 17:44:38 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
m = n // 2

def factorial(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k

ans = 0
for i in range(n + 1):
    for j in range(m + 1):
        if n == i + 2*j:
            ans += factorial(i + j) // (factorial(i) * factorial(j)) % 10007

print(int(ans) % 10007)
