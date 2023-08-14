import sys
from collections import deque

def can_move(x, y, a, b):
    for i in range(x, x + a):
        for j in range(y, y + b):
            if graph[i][j]:
                return False

    return True

input = sys.stdin.readline

N, M, A, B, K = map(int, input().split())

graph = [[0] * M for _ in range(N)]
visited = set()

for _ in range(K):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

s_x, s_y = map(int, input().split())
e_x, e_y = map(int, input().split())

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

q = deque()
q.append((s_x - 1, s_y - 1, 0))
visited.add((s_x - 1, s_y - 1))

while q:
    x, y, c = q.popleft()
    if x == e_x - 1 and y == e_y - 1:
        print(c)
        exit(0)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if (nx, ny) in visited:
            continue

        if nx < 0 or ny < 0 or nx + A - 1 >= N or ny + B - 1 >= M:
            continue

        if can_move(nx, ny, A, B):
            q.append((nx, ny, c + 1))
            visited.add((nx, ny))

print(-1)