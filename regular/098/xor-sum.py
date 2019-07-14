N = int(input())
ints = [int(x) for x in input().split()]

ans = 0
r = 0
s = 0
xs = 0
for l in range(N):
    while r < N and s + ints[r] == xs ^ ints[r]:
        s += ints[r]
        xs ^= ints[r]
        r += 1
    ans += (r - l)
    s -= ints[l]
    xs ^= ints[l]

print(ans)
