testcases = int(input())

map = dict()
while(testcases):
    val = input()
    if val in map:
        print("YES")
    else:
        print("NO")
        map[val] = True
    testcases -=1
