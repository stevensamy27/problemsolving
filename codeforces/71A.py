n = int(input())


def solve(s):
    if len(s) <= 10:
        return s

    return s[0]+str(len(s)-2)+s[len(s)-1]

for i in range(n):
    s = input()
    print(solve(s))