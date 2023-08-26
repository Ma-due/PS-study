import sys
from collections import deque


def bfs(i, j):
    global answer
    checked = [[0] * M for _ in range(N)]
    q = deque()
    q.append((i, j, 0))
    checked[i][j] = 1

    while q:
        x, y, c = q.popleft()
        answer = max(answer, c)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 > nx or 0 > ny or nx >= N or ny >= M or grid[nx][ny] == 'W' or checked[nx][ny]: continue
            checked[nx][ny] = 1
            q.append((nx, ny, c + 1))



input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

answer = -1
for i in range(N):
    for j in range(M):
        if 0 <= i - 1 < N and 0 <= i + 1 < N:
            if grid[i - 1][j] == 'L' and grid[i + 1][j] == 'L':
                continue
        if 0 <= j - 1 < M and 0 <= j + 1 < M:
            if grid[i][j - 1] == 'L' and grid[i][j + 1] == 'L':
                continue

        if grid[i][j] == 'L': bfs(i, j)

print(answer)
