#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1012                           #+#        #+#      #+#     #
#    Solved: 2025/02/10 18:11:06 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    pos = {}
    dic = {i: [] for i in range(K)}
    for i in range(K):
        x, y = map(int, input().split())
        for k, v in pos.items():
            if (abs(v[0] - x) == 1 and abs(v[1] - y) == 0) or (abs(v[0] - x) == 0 and abs(v[1] - y) == 1):
                dic[i].append(k)
                dic[k].append(i)
        pos[i] = (x, y)

    cnt = 0
    e = set(range(K))
    visited = set()
    while e:
        k = e.pop()
        visited.add(k)

        stack = set()
        stack.update(dic[k])

        while stack:
            case = stack.pop()
            if case not in visited:
                stack.update(dic[case])
                visited.add(case)
        
        e -= visited
        cnt += 1

    print(cnt)
