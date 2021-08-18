# Solution to problem: https://codeforces.com/contest/1551/problem/A
# Tags: [Basic Math]

testcases = int(input())

for testcase in range(testcases):
    n = int(input())
    partial = n // 3
    mod = n % 3

    if mod == 0:
        print(partial , partial)
    elif mod == 1:
        print(partial + 1 , partial)
    else:
        print(partial , partial + 1)