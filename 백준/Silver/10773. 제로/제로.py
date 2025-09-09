# 10773

import sys
n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    s = int(sys.stdin.readline())

    if(s==0): stack.pop()
    else: stack.append(s)

print(sum(stack))