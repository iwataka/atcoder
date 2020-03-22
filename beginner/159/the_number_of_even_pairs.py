def comb2(n):
    if n < 2:
        return 0
    return int(n * (n - 1) / 2)

n, m = map(int, input().split())
print(comb2(n) + comb2(m))
