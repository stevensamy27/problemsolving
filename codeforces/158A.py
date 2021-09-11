n,k = map(int,input().split())
a = list(map(int,input().split()))
cou = 0

for i in range(n):
    if a[k-1] == 0 and a[i] == a[k-1]:
        cou = cou+0
    elif a[k-1] <= a[i]:
        cou = cou+1
    else:    
        cou = cou+0
print(cou)
        
