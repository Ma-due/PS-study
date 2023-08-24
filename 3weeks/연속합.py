import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

pre_sum = 0
answer = -float('inf')
for i in range(N):
    pre_sum += lst[i]

    answer = max(answer, pre_sum)

    if pre_sum < 0:
        pre_sum = 0

print(answer)