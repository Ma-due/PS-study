import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

land = []

target = ()
for i in range(n):
    land.append(list(map(int, input().split())))
    if 2 in land[i]:
        target = (i, land[i].index(2), 0)

answer = [[0] * m for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

q = deque()
visited = set()

q.append(target)
visited.add((target[0], target[1]))
while q:
    x, y, c = q.popleft()

    answer[x][y] = c
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) not in visited and land[nx][ny] == 1:
                q.append((nx, ny, c + 1))
                visited.add((nx, ny))

for i in range(n):
    for j in range(m):
        if land[i][j] == 1 and answer[i][j] == 0:
            answer[i][j] = -1

for arr in answer:
    print(' '.join(list(map(str,arr))))