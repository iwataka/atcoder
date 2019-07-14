n, x = map(int, input().split())
ms = []
for _ in range(n):
    ms.append(int(input()))
ans = (x - sum(ms)) // min(ms) + len(ms)
print(ans)
