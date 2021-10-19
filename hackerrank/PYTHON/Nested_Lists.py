if __name__ == '__main__':
    n = int(input())
    my_array = []
    for i in range(n):
        a , b = input() , float(input())
        my_array.append((b,a))
        
    my_array.sort()
    lowest = my_array[0]
    flag = True
    target = 0
    for i in my_array:
        if i[0] != lowest[0] and flag:
            target = i[0]
            flag = False
            
        if i[0] == target:
            print(i[1])
