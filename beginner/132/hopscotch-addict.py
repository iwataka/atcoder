def add_edge(s, d, edges):
    if s in edges:
        edges[s].append(d)
    else:
        edges[s] = [d]


N, M = [int(x) for x in input().split()]
edges = {}
for _ in range(M):
    s, d = [int(x) for x in input().split()]
    add_edge(s*3 + 0, d*3 + 1, edges)
    add_edge(s*3 + 1, d*3 + 2, edges)
    add_edge(s*3 + 2, d*3 + 0, edges)
S, T = [int(x)*3 + 0 for x in input().split()]

reached = set()
curs = [S]
count = 0
success = False

while curs:
    if T in curs:
        success = True
        break
    nexts = []
    for c in curs:
        if not c in edges:
            continue
        ns = edges[c]
        for n in ns:
            if not n in reached:
                reached.add(n)
                nexts.append(n)
    curs = nexts
    count += 1

if success:
    print(count // 3)
else:
    print(-1)
