#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1463                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1463                           #+#        #+#      #+#     #
#    Solved: 2025/02/10 14:33:18 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())

cnt = 0
if N == 1:
    print(0)
    q = []
else:
    q = set()
    q.add(N)

while q:
    rq = set()
    for n in q:
        if n % 2 == 0:
            ans = n / 2
            if ans == 1:
                print(cnt + 1)
                rq = []
                break
            else:
                rq.add(ans)
        if n % 3 == 0:
            ans = n / 3
            if ans == 1:
                print(cnt + 1)
                rq = []
                break
            else:
                rq.add(ans)
        ans = n - 1
        if ans == 1:
            print(cnt + 1)
            rq = []
            break
        else:
            rq.add(ans)

    q = rq
    cnt += 1
