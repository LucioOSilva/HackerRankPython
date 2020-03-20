"""
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
"""

n = int(input())
s = set(map(int, input().split()))

soma = 0

if len(s) == n:
    try:
        f = int(input())
    except (ValueError, TypeError):
        pass
    else:
        for c in range(f):
            task = input().split()
            if task[0] == 'pop':
                s.pop()
            elif task[0] == 'remove':
                try:
                    s.remove(int(task[1]))
                except (KeyError, IndexError):
                    pass
            elif task[0] == 'discard':
                s.discard(int(task[1]))
for c in s:
    soma += c
print(soma)