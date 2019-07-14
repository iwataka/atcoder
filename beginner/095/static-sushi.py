def solve(c, sushis):
    clockwise = solve_one_direction(c, sushis, True)
    counter = solve_one_direction(c, sushis[::-1], False)
    return max(clockwise, counter)

def solve_one_direction(c, sushis, clockwise=True, already_turn=False):
    total_v = 0
    max_v = 0
    for i, sushi in enumerate(sushis):
        total_v += sushi[1]
        x = sushi[0] if clockwise else c - sushi[0]
        v = total_v - x
        if max_v < v:
            max_v = v
        if not already_turn and x <= c / 2:
            rev = v - x + solve_one_direction(c, sushis[i + 1::][::-1], not clockwise, True)
            if max_v < rev:
                max_v = rev

    return max_v


n, c = map(int, input().split())
sushis = []
for _ in range(n):
    sushis.append([int(x) for x in input().split()])
print(solve(c, sushis))
