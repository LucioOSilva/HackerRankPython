try:
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
except (ValueError, TypeError) as error:
    print(f'An Error occurred, {error}')
else:
    print([[r, s, t] for r in range(x+1) for s in range(y+1) for t in range(z+1) if r + s + t != n])
