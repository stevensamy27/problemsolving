'''
N = input()

from collections import Counter
def isuni (N):
    A = Counter(N)
 
    if(len(A) == len(N)):
        if len(N)%2==0:
            return "CHAT WITH HER!"
    else:
         if len(N)%2==0:
            return "IGNORE HIM!"

    if(len(A) == len(N)):
        if len(N)%2!=0:
            return "IGNORE HIM!"
    else:
         if len(N)%2!=0:
            return "CHAT WITH HER!"        
print(isuni(N))
'''

N = input()
def IS_UNIQUE(str):

	a = set(str)

	return len(a)

if __name__ == "__main__":

    D = IS_UNIQUE(N)

if D%2==0:
    print ("CHAT WITH HER!")
else:
    print ("IGNORE HIM!")

