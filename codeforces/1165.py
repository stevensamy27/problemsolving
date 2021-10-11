x = int(input())
y = [int(x) for x in input().split()]
z = x - 1
for i in range(10):

    if z in y:
        print (z)
        break
    else:    
        z = z-1
 