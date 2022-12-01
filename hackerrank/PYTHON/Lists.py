if __name__ == '__main__':
    N = int(input())       
    the_List = list() 


    for i in range(N): 
        order = input()
        the_number = int(input())

        if(order == 'print'):
            print(the_List)
        elif(order == 'append'): 
            the_List.append(the_number)
        elif(order == 'pop'): 
            the_List.pop(the_number)
        elif(order == 'remove'): 
            the_List.remove(the_number)
        elif(order == 'sort'): 
            the_List.sort()
        
        
    print(the_List)

