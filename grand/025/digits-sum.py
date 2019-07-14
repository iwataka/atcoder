def solve(N):
    digits = [int(d) for d in str(N)]
    tmp_ans = sum(digits)
    if tmp_ans == 1:
        return 10
    else:
        return tmp_ans

# assert(solve(2) == 2) # 1 and 1
# assert(solve(10) == 10) # 5 and 5
# assert(solve(15) == 6) # 2 and 13
# assert(solve(100) == 10) # 50 and 50
# assert(solve(100000) == 10) # 50000 and 50000

N = input()
print(solve(N))
