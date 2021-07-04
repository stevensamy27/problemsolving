N = int(input())

ret = 0 

for i in range(0, N):
    k = 0 
    l = x, y, z = [int(a) for a  in input().split()] 
    k= x+y+z
    if k >= 2:
        ret += 1
        
print(ret) 