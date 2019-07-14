def split_by_floor(arr, floor):
    ans = []
    tmp = []
    for e in arr:
        if e < floor and tmp:
            ans.append(tmp)
            tmp = []
        else:
            tmp.append(e)
    if tmp:
        ans.append(tmp)
    return ans

N, K, Q = map(int, input().split())
arr = [int(x) for x in input().split()]

floor_cands = list(sorted(set(arr)))
ans = floor_cands[-1] - floor_cands[0]

for floor in floor_cands:
    splitted_arrs = split_by_floor(arr, floor)
    cands = []
    for splitted in splitted_arrs:
        cands.extend(sorted(splitted)[:len(splitted) - K + 1])
    if len(cands) < Q:
        continue
    sorted_cands = list(sorted(cands))
    tmp_ans = sorted_cands[Q - 1] - sorted_cands[0]
    if ans > tmp_ans:
        ans = tmp_ans

print(ans)
