def is_kaibun(s):
    half = int(len(s) / 2) if len(s) % 2 == 0 else int((len(s) + 1) / 2)
    for i in range(half):
        if s[i] != s[-(i + 1)]:
            return False
    return True


s = input()
s1 = s[:int((len(s) - 1) / 2)]
s2 = s[int(((len(s) + 3) / 2) - 1):]
result = is_kaibun(s) and is_kaibun(s1) and is_kaibun(s2)
print('Yes' if result else 'No')
