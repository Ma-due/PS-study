import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline

def rotated(list):
    return [[row[i] for row in list[::-1]] for i in range(len(list[0]))]

def spin(list):
    global answer

    for _ in range(4):
        list[0] = rotated(list[0])
        for _ in range(4):
            list[1] = rotated(list[1])
            for _ in range(4):
                list[2] = rotated(list[2])
                for _ in range(4):
                    list[3] = rotated(list[3])
                    for _ in range(4):
                        list[4] = rotated(list[4])

                        if list[0][0][0] == 1 and list[4][4][4] == 1:
                            count = bfs(list)
                            if count == 12:
                                print(12)
                                exit(0)
                            answer = min(count, answer)

def bfs(list):
    dz, dx, dy = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    q = deque()
    visited = set()

    q.append((0, 0, 0, 0))
    visited.add((0, 0, 0))

    while q:
        z, x, y, c = q.popleft()

        if z == 4 and x == 4 and y == 4:
            return c

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if list[nz][nx][ny] == 1 and (nz, nx, ny) not in visited:
                    q.append((nz, nx, ny, c + 1))
                    visited.add((nz, nx, ny))

    return float('inf')

answer = float('inf')
origin = []
for i in range(5):
    new_list = []
    for j in range(5):
        new_list.append(list(map(int, input().split())))

    origin.append(new_list)

perm = permutations([0, 1, 2, 3, 4])

for p in perm:
    new_maze = []
    for i in p:
        new_maze.append(origin[i])

    spin(new_maze)

print(answer if answer != float('inf') else -1)
