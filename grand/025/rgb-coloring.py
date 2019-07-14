import math

N, A, B, K = map(int, input().split())

ab_patterns = []
max_a = K // A
for a_count in range(max_a + 1):
    remaining = K - A * a_count
    if remaining % B == 0:
        b_count = remaining // B
        ab_patterns.append((a_count, remaining // B))

ans_ceil = 998244353

ans = 0
for a_count, b_count in ab_patterns:
    result = None
    for n_greens in range(min(a_count, b_count), -1, -1):
        n_reds = a_count - n_greens
        n_blues = b_count - n_greens
        if n_greens + n_reds + n_blues > N:
            break
        n_nocolors = N - n_reds - n_greens - n_blues
        # print(n_greens, n_reds, n_blues, n_nocolors)
        if result:
            result *= (n_greens + 1)
            result //= n_reds
            result //= n_blues
            result *= (n_nocolors + 1)
        else:
            result = math.factorial(N) // (math.factorial(n_greens) * math.factorial(n_reds) * math.factorial(n_blues) * math.factorial(n_nocolors))
        ans += result
        if ans > ans_ceil:
            ans %= ans_ceil

print(ans)
