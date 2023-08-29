import sys

input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

stack = []
bl = len(bomb)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-bl:]) == bomb:
        for _ in range(bl):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
