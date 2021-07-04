N = int(input())

ret = 0 
for i in range(0, N):
    k = 0 
    l = x, y, z = [int(a) for a  in input("Enter a three value: ").split()] 
    k= x+y+z
    if k >= 2:
        ret += 1

print(ret)

'''
if N == 1:
    x, y, z = [int(a) for a  in input("Enter a three value: ").split()]  
    print(x+z+y)
  
elif N == 2:
    x, y, z = input("Enter a three value: ").split()
    x, y, z = input("Enter a three value: ").split()
    if (x, y, z,) != (1 or 0):
         print("please enter 1 or 0")
    else: 
        print(x+z+y)
  
elif N == 3:
        x, y, z = input("Enter a three value: ").split()
        x, y, z = input("Enter a three value: ").split()
        x, y, z = input("Enter a three value: ").split()

        if (x, y, z,) != (1 or 0):
            print("please enter 1 or 0")
        else: 
            print(x+z+y)
  
else:
    print ("55555555555555") 
'''

