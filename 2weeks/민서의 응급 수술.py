import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
answer = 0
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        answer += 1

count_tree = set()
for i in range(1, n + 1):
    count_tree.add(find(i))

print(answer + len(count_tree) - 1)