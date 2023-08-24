import sys
import bisect

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 0
for i in range(N):
    temp = lst[:i] + lst[i + 1:]
    left, right = 0, len(temp) - 1

    while left < right:
        pre_sum = temp[left] + temp[right]

        if pre_sum == lst[i]:
            answer += 1
            break
        elif pre_sum < lst[i]:
            left += 1
        else:
            right -= 1

print(answer)