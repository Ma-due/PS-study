import sys
import heapq

input = sys.stdin.readline

offer = []
n = int(input())
for _ in range(n):
    offer.append(list(map(int, input().split())))

offer.sort(key=lambda x: x[1])

answer = []
for p, d in offer:
    heapq.heappush(answer, p)
    if len(answer) > d:
        heapq.heappop(answer)

print(sum(answer))

"""
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10

5
10 1
30 3
30 3
30 3
30 3
30 3
"""