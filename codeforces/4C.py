x = int(input())
dectionary = dict()


for i in range(x):
    string = str(input())
    if  string not in dectionary:
        print("OK")
        dectionary[string] = 1    
    else :
        value = dectionary[string]
        # print(string , value)
        print("{0}{1}".format(string, value))
        dectionary[string] = value + 1


