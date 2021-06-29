n = input()
vowels = ["a", "o", "y", "e", "u", "i"] 

val = ""
for  i in n:
    i = i.lower()

    if i not in vowels:
        print("."+ i , end='')

