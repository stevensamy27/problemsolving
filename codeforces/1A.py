N = int(input ("Width of theater = ",))
M = int(input ("height of theater =",))  
A = int(input("flagstone =", ))
x = N/A
z = M/A

if N%A != 0:
    x=x+1
if M%A != 0:
    z=z+1

print(z+x-1)