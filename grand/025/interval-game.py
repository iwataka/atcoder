N = int(input())

intervals = []
for _ in range(N):
    l, r = map(int, input().split())
    intervals.append((l, r))

ans = 0
pos = 0
while intervals:
    max_dist = -1
    max_index = -1
    max_pos = 0
    for i, interval in enumerate(intervals):
        l, r = interval
        l_dist = abs(l - pos)
        r_dist = abs(r - pos)
        dist = 0 if l <= pos <= r else min(l_dist, r_dist)
        if max_dist < dist:
            max_dist = dist
            max_index = i
            max_pos = pos if dist == 0 else (l if l_dist < r_dist else r)
    del intervals[max_index]
    ans += max_dist
    pos = max_pos

print(ans + abs(pos))
