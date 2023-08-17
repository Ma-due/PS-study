import sys
from collections import deque

def bfs(start):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    q = deque()
    q.append((start[0], start[1]))

    visited = set()
    visited.add((start[0], start[1]))

    melt = set()
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited:
                    if grid[nx][ny] == 0:
                        q.append((nx, ny))

                    visited.add((nx, ny))

                else:
                    if grid[nx][ny] == 1:
                        melt.add((nx, ny))

    if melt:
        for x, y in melt:
            grid[x][y] = 0

        return True

    return False

input = sys.stdin.readline

N, M = map(int, input().split())

grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

time = 0

while bfs((0, 0)):
    time += 1

print(time)