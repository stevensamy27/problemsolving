x = int(input())
array = [int(x) for x in input().split()]

array.sort()

day = 1
for i in array:
    if i >= day:
        day += 1

print(day - 1)

# x = int(input())
# y = [int(x) for x in input().split()]
# output = set()
# for i in y:
#         output.add(i)
# print (len(output))



# x = int(input())
# y = [int(x) for x in input().split()]
# z = 1
# output = 0
# for i in range(x):
#     if z in y:
#        output = output + 1  
#        z = z + 1  
#     else:    
#         z = z + 1   
# print(output)

 