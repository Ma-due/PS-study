import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = []
for _ in range(N):
    belt.append(int(input()))

dict = defaultdict(int)

left = 0
right = k - 1

dict[c] += 1

for i in range(right + 1):
    dict[belt[i]] += 1

answer = 0
while left < N:
    answer = max(answer, len(dict))

    dict[belt[left]] -= 1
    if (dict[belt[left]] == 0):
        del dict[belt[left]]
    left += 1

    right += 1
    dict[belt[right % N]] += 1

print(answer)