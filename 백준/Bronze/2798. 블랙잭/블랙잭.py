#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2798                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: derveroncia <boj.kr/u/derveroncia>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2798                           #+#        #+#      #+#     #
#    Solved: 2025/01/31 16:04:04 by derveroncia   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, M = map(int, input().split())
cards = list(map(int, input().split()))

while True:
    if M <= max(cards) + min(cards):
        cards.remove(max(cards))
    else:
        break

num = len(cards)

answer = M
for i in range(num-2):
    for j in range(i+1, num-1):
        for k in range(j+1, num):
            a = cards[i] + cards[j] + cards[k]
            if M < a:
                continue
            else:
                if answer > M - a:
                    answer = M - a

print(M - answer)