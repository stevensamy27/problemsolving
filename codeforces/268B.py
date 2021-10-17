n = int(input())
z=n
x = 0
for i in range (n):
    n=n-1
    if n > 1:
        x = x+2
    else:
        print (z+x+2)