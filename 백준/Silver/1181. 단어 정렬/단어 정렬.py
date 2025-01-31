#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:51:34 by deveronica   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

words = []
for _ in range(N):
    words.append(word) if (word := input()) not in words else None

ans = sorted(words, key=lambda x: (len(x), x))
print(*ans, sep="\n")
