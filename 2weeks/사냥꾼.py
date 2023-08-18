import sys

input = sys.stdin.readline

M, N, L = map(int, input().split())
spot = list(map(int, input().split()))
spot.sort()

answer = 0
for _ in range(N):
    x, y = map(int, input().split())
    start = 0
    end = len(spot) - 1

    if y > L:
        continue

    while start < end:
        mid = (start + end) // 2

        if spot[mid] < x:
            start = mid + 1
        else:
            end = mid

    if abs(spot[end] - x) + y <= L or abs(spot[end - 1] - x) + y <= L:
        answer += 1

print(answer)
