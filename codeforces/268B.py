n = int(input())
z=n
x = 0
for i in range(n-1):
    x = x + 2
    print (x)

# print(n+(x*2))






'''
Input = 3

    |  |  |
n   x  x  y
1   x     y
2      y
3   y 

Output = 7 

'''
#  #  #  #  #  #  #  #  #  #  #  #  #  

'''
Input = 4

    |  |  |  |
n   x  x  x  y
1   x        y
2      x     y  
3         y
4   x     y  y
5      y
6   y

Output = 14

'''

#  #  #  #  #  #  #  #  #  #  #  #  #  


'''
Input = 5

    |  |  |  |  |
n   x  x  x  x  y
1   x           y
2      x        y  
3         x     y
4            y
5   x        y  y
6      x     y  y
7         y
8   x     y  y  y
9      y
10  y

Output = 25

'''