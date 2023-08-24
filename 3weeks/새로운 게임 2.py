import sys

def blue(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    else: return 2

input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
n_grid = [[[] for _ in range(N)] for _ in range(N)]
nights = []

for i in range(K):
    x, y, d = map(lambda x: int(x) - 1, input().split())
    nights.append([x, y, d])
    n_grid[x][y].append(i)

turn = 1
while turn < 1000:
    for i in range(K):
        x, y, d = nights[i]
        nx, ny = x + dx[d], y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or grid[nx][ny] == 2:
            d = blue(d)

            nights[i][2] = d
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or grid[nx][ny] == 2:
                continue

        move_list = []
        for j, n_index in enumerate(n_grid[x][y]):
            if n_index == i:
                move_list.extend(n_grid[x][y][j:])
                n_grid[x][y] = n_grid[x][y][:j]
                break

        if grid[nx][ny] == 1:
            move_list.reverse()

        for h in move_list:
            n_grid[nx][ny].append(h)
            nights[h][0], nights[h][1] = nx, ny

        if len(n_grid[nx][ny]) >= 4:
            print(turn)
            exit(0)

    turn += 1

print(-1)