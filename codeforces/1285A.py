n = int(input())
s = input()
 
max_l, max_r = 0, 0
for i in s:
  if i == 'R':
    max_r += 1
  else:
    max_l += 1
 
print(max_r + max_l + 1)