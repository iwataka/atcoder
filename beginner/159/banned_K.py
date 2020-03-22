N = int(input())
As = list(map(int, input().split()))

num_count = {}
count_comb = {}
num_ans = {}
sum_combs = 0

def comb2(n):
    if n not in count_comb:
        count_comb[n] = (n * (n - 1)) // 2
    return count_comb[n]

def ans(ex_num):
    ex_count = num_count[ex_num]
    return sum_combs + comb2(ex_count - 1) - comb2(ex_count)
    # if ex_num in num_ans:
    #     return num_ans[ex_num]

    # result = 0
    # for n, c in num_count.items():
    #     if n == ex_num:
    #         result += comb2(c - 1)
    #     else:
    #         result += comb2(c)
    # num_ans[ex_num] = result
    # return result


for a in As:
    if a not in num_count:
        num_count[a] = 0
    num_count[a] += 1

for _, c in num_count.items():
    sum_combs += comb2(c)

for a in As:
    print(ans(a))
