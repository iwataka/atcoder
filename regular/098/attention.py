N = int(input())
queue = [x for x in input()]

n_wests = 0
n_easts = queue.count('E') - (1 if queue[0] == 'E' else 0)
min_i = 0
min_n_changes = n_easts
for i in range(1, N):
    prev_dir = queue[i - 1]
    cur_dir = queue[i]
    if prev_dir == 'W':
        n_wests += 1
    if cur_dir == 'E':
        n_easts -= 1
    n_changes = n_wests + n_easts
    if n_changes < min_n_changes:
        min_n_changes = n_changes
        min_i = i

print(min_n_changes)
