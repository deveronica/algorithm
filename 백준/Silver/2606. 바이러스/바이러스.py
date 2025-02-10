#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: deveronica <boj.kr/u/deveronica>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2025/02/10 15:39:26 by deveronica    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
L = int(input())

dic = {k: [] for k in range(1, N+1)}
for _ in range(L):
    a, b = map(int, input().split())
    dic.get(a).append(b)
    dic.get(b).append(a)

answer = set()
answer.update(dic[1])
search = set()
search.update(dic[1])
searched = []

while search:
    new_search = set()
    searched.extend(search)
    for case in search:
        answer.update(dic[case])
        for new_case in dic[case]:
            if new_case not in searched:
                new_search.add(new_case)
    search = new_search

print(len(answer) - 1 if len(answer) >= 2 else 0)