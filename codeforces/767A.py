n = int(input())
a = list(map(int,input().split()))

curr = []
not_curr = []
last = 0

for i in a:
    if i == n:
        print(i )
        index = a.index(i)
        if index > 0:
            x = index - 1
            print (x)   
            if x == i-1:
                print(i , i-1)
                print("yes")  
    else:
        print('\n', end='')
        not_curr.append(i)
        if not_curr == i-1:
            print (not_curr)
    

print(not_curr)



# def prints(n):
#     for i in range(n):
#         print('\n', end='')
        
# def printy(n):
#     for i in range(len(n) - 1, -1 , -1):
#         print(n[i], end=' ')
#     print()
 
# for i in a:
#     if i > last:
#         last = i
#         curr.append(i)
#     else:
#         prints(len(curr) - 1)
#         printy(curr)
 
 
#         curr = [i]
#         last = i
 
# prints(len(curr) - 1)
 
# printy(curr)