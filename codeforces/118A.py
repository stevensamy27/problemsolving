n = input()
vowels = ["a", "o", "y", "e", "u", "i"] 

val = ""
for i in n:
    i = i.lower()
    partial = ""
    if i not in vowels:
        partial = "."+i
    else:
        partial = ""
    
    if partial:
        val += partial
print(val)