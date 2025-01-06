def abc(n):
    for a in range(int(n**0.5) + 1):
        for b in range(int((n - a**2)**0.5) + 1):
            for c in range(int((n - a**2 - b**2)**0.5) + 1):
                d2 = n - a**2 - b**2 - c**2
                if d2 >= 0:
                    d = int(d2**0.5)
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return (a, b, c, d)

n = int(input())
print(*abc(n))
